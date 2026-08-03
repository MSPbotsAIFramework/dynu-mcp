import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool()
    async def dynu_get_details_domain_registration_domain(id: int) -> str:
        """Get details of a domain registration domain.

        API: GET /domain/{id}

        Args:
            id: Required. The id of the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_domains_domain_registration_service() -> str:
        """Get a list of domains for domain registration service.

        API: GET /domain

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/domain", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
