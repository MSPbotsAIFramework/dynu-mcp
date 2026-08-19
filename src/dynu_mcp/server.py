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
        instructions=(
            "Dynu is a dynamic DNS, domain registration, email hosting, and cloud "
            "compute (VPS) provider. This server exposes 6 tool domains over the "
            "account's Dynu services: dns (manage DNS services and their records — "
            "dynu_get_list_domains_dns_service is the endpoint MSPbots itself uses); "
            "domain (read-only lookup of registered domains); email (manage email "
            "services and their mailbox accounts); compute (manage VPS instances — "
            "start/stop act on live infrastructure and are destructive/irreversible); "
            "monitor (manage uptime/service monitors — add/delete, pause/unpause, "
            "and account limits); ping (connectivity check against the Dynu API "
            "itself, useful for verifying credentials before other calls). Typical "
            "flow: call a list tool (e.g. dynu_get_list_domains_dns_service, "
            "dynu_get_list_email_services, dynu_get_list_instances, "
            "dynu_get_list_monitors) to find a service/resource ID, then pass that "
            "ID to the matching detail/record/account tool. Write and delete tools "
            "act on real production DNS records, mailboxes, monitors, and VPS "
            "instances — always use IDs returned by a prior list/get call, never "
            "guess them."
        ),
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
