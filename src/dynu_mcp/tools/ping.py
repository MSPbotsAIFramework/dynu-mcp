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
    async def dynu_ping_api_server_obtain_pong_response_get(
        message: Annotated[str, Field(description="Message to receive back in the pong reply.")],
    ) -> str:
        """Ping the Dynu API server (GET) and get back a pong response. Useful for verifying credentials."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get("/ping", params={"message": message})
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_ping_api_server_obtain_pong_response_post(
        body: Annotated[
            dict,
            Field(
                description=(
                    "Request payload — see Dynu's OpenAPI spec (Models section) "
                    "for the exact field names/types of this resource."
                )
            ),
        ],
    ) -> str:
        """Ping the Dynu API server (POST) and get back a pong response. Useful for verifying credentials."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.post("/ping", json_body=body)
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()
