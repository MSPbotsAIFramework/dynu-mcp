from collections.abc import Callable
from typing import Annotated

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from .._json import dump_json_capped
from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN

_BODY_DESC = (
    "Request payload — see Dynu's OpenAPI spec (Models section) for the "
    "exact field names/types of this resource."
)


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool(annotations=ToolAnnotations(idempotentHint=False))
    async def dynu_add_new_monitor(
        body: Annotated[dict, Field(description=_BODY_DESC)],
    ) -> str:
        """Add a new uptime/service monitor."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.post("/monitor", json_body=body)
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(destructiveHint=True, idempotentHint=True))
    async def dynu_delete_monitor(
        id: Annotated[int, Field(description="ID of the monitor to delete.")],
    ) -> str:
        """Delete a monitor. Irreversible."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.delete(f"/monitor/{id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_details_monitor(
        id: Annotated[int, Field(description="ID of the monitor.")],
    ) -> str:
        """Get details of a single monitor."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/monitor/{id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_list_monitors() -> str:
        """List all monitors on the account."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get("/monitor")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_limits_associated_monitoring() -> str:
        """Get the account's monitoring plan limits (e.g. max monitors)."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get("/monitor/limit")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(idempotentHint=True))
    async def dynu_pause_monitor(
        id: Annotated[int, Field(description="ID of the monitor to pause.")],
    ) -> str:
        """Pause a monitor so it stops checking and alerting."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/monitor/{id}/pause")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(idempotentHint=True))
    async def dynu_unpause_monitor(
        id: Annotated[int, Field(description="ID of the monitor to unpause.")],
    ) -> str:
        """Resume a paused monitor so it starts checking and alerting again."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/monitor/{id}/unpause")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()
