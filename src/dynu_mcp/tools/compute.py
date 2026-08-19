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
    async def dynu_get_instance(
        id: Annotated[int, Field(description="ID of the compute instance.")],
    ) -> str:
        """Get details of a single compute (VPS) instance by ID."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/compute/instance/{id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_list_instances() -> str:
        """List all compute (VPS) instances on the account."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get("/compute/instance")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(destructiveHint=True, idempotentHint=True))
    async def dynu_start_instance(
        id: Annotated[int, Field(description="ID of the compute instance to start.")],
    ) -> str:
        """Start a compute (VPS) instance. Acts on live infrastructure."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/compute/instance/{id}/start")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(destructiveHint=True, idempotentHint=True))
    async def dynu_stop_suspend_instance(
        id: Annotated[int, Field(description="ID of the compute instance to stop/suspend.")],
    ) -> str:
        """Stop (suspend) a compute (VPS) instance. Acts on live infrastructure."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/compute/instance/{id}/stop")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()
