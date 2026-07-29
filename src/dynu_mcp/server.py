import contextvars
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from .api_client import DynuClient
from .config import Settings

# Per-request credential isolation via contextvars.
# GatewayTokenMiddleware sets this before the MCP handler runs.
# Python asyncio copies context per task, so concurrent SSE connections are isolated.
_gateway_creds_var: contextvars.ContextVar[str | None] = contextvars.ContextVar(
    "dynu_gateway_creds", default=None
)


def get_client_from_context(settings: Settings) -> DynuClient | None:
    """Resolve the active DynuClient for the current request context."""
    api_key = _gateway_creds_var.get()
    if not api_key:
        return None
    return DynuClient(api_key, settings.dynu_base_url)


class GatewayTokenMiddleware:
    """ASGI middleware.

    Reads X-Dynu-Api-Key (required) from request headers and stores it in
    the contextvar. Returns 401 if the header is missing on /mcp requests.
    """

    def __init__(self, app: ASGIApp, settings: Settings):
        self.app = app
        self.settings = settings

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "")
        if not path.startswith("/mcp"):
            await self.app(scope, receive, send)
            return

        request = Request(scope)
        api_key = request.headers.get("x-dynu-api-key")
        if not api_key:
            response = JSONResponse(
                {
                    "error": "Missing credentials",
                    "message": "This server requires the X-Dynu-Api-Key header",
                    "required_headers": ["X-Dynu-Api-Key"],
                    "optional_headers": [],
                },
                status_code=401,
            )
            await response(scope, receive, send)
            return

        ctx_token = _gateway_creds_var.set(api_key)
        try:
            await self.app(scope, receive, send)
        finally:
            _gateway_creds_var.reset(ctx_token)


def create_mcp_server(settings: Settings) -> FastMCP:
    """Build the FastMCP server instance and register all Dynu tools."""
    # DNS-rebinding protection is a browser-oriented safeguard that rejects
    # non-localhost Host headers with 421. Disable it so the server works
    # correctly behind a reverse proxy or docker network.
    mcp = FastMCP(
        name="dynu-mcp",
        transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
    )

    client_factory: Callable[[], DynuClient | None] = lambda: get_client_from_context(settings)

    from .tools import compute, dns, domain, email, monitor, ping

    dns.register(mcp, client_factory)
    domain.register(mcp, client_factory)
    email.register(mcp, client_factory)
    monitor.register(mcp, client_factory)
    ping.register(mcp, client_factory)
    compute.register(mcp, client_factory)

    return mcp
