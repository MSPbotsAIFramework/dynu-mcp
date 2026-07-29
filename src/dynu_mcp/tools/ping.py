import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool()
    async def dynu_ping_api_server_obtain_pong_response_get(message: str) -> str:
        """Ping the API server to obtain the pong response.

        API: GET /ping

        Args:
            message: Required. The message to receive back in pong.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"message": message}
        try:
            result = await client.get("/ping", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_ping_api_server_obtain_pong_response_post(body: dict) -> str:
        """Ping the API server to obtain the pong response.

        API: POST /ping

        Args:
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/ping", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
