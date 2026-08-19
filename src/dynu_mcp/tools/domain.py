from collections.abc import Callable
from typing import Annotated

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from .._json import dump_json_capped
from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_details_domain_registration_domain(
        id: Annotated[int, Field(description="ID of the registered domain.")],
    ) -> str:
        """Get details of a single domain-registration domain by ID."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/domain/{id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_list_domains_domain_registration_service() -> str:
        """List all domains registered through the domain-registration service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get("/domain")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()
