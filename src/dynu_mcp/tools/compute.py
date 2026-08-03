import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool()
    async def dynu_get_instance(id: int) -> str:
        """Get an instance.

        API: GET /compute/instance/{id}

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_instances() -> str:
        """Get a list of instances.

        API: GET /compute/instance

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/compute/instance", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_start_instance(id: int) -> str:
        """Start an instance.

        API: GET /compute/instance/{id}/start

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/start"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_stop_suspend_instance(id: int) -> str:
        """Stop (suspend) an instance.

        API: GET /compute/instance/{id}/stop

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/stop"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
