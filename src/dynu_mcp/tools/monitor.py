import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool()
    async def dynu_add_new_monitor(body: dict) -> str:
        """Add a new monitor.

        API: POST /monitor

        Args:
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/monitor", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_delete_monitor(id: int) -> str:
        """Delete a monitor.

        API: DELETE /monitor/{id}

        Args:
            id: Required. The id of the monitor.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/monitor/{id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_details_monitor(id: int) -> str:
        """Get details of a monitor.

        API: GET /monitor/{id}

        Args:
            id: Required. The id of the monitor.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/monitor/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_monitors() -> str:
        """Get a list of monitors.

        API: GET /monitor

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/monitor", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_limits_associated_monitoring() -> str:
        """Limits associated with monitoring.

        API: GET /monitor/limit

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/monitor/limit", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_pause_monitor(id: int) -> str:
        """Pause a monitor.

        API: GET /monitor/{id}/pause

        Args:
            id: Required. The id of the monitor.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/monitor/{id}/pause"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_unpause_monitor(id: int) -> str:
        """Unpause a monitor.

        API: GET /monitor/{id}/unpause

        Args:
            id: Required. The id of the monitor.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/monitor/{id}/unpause"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
