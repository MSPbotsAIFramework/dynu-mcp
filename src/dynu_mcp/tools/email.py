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
    async def dynu_add_new_email_account_email_service(
        id: Annotated[int, Field(description="ID of the email service.")],
        body: Annotated[dict, Field(description=_BODY_DESC)],
    ) -> str:
        """Add a new mailbox account to an email service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.post(f"/email/{id}/account", json_body=body)
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_details_email_account(
        id: Annotated[int, Field(description="ID of the email service.")],
        account_id: Annotated[int, Field(description="ID of the email account.")],
    ) -> str:
        """Get details of a single mailbox account on an email service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/email/{id}/account/{account_id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_details_email_service(
        id: Annotated[int, Field(description="ID of the email service.")],
    ) -> str:
        """Get details of a single email service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/email/{id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_list_email_accounts_email_service(
        id: Annotated[int, Field(description="ID of the email service.")],
    ) -> str:
        """List all mailbox accounts on an email service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/email/{id}/account")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_list_email_services() -> str:
        """List all email services on the account."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get("/email")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(destructiveHint=True, idempotentHint=True))
    async def dynu_remove_email_account_email_service(
        id: Annotated[int, Field(description="ID of the email service.")],
        account_id: Annotated[int, Field(description="ID of the email account to remove.")],
    ) -> str:
        """Remove a mailbox account from an email service. Irreversible."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.delete(f"/email/{id}/account/{account_id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(idempotentHint=True))
    async def dynu_update_existing_email_account_email_service(
        id: Annotated[int, Field(description="ID of the email service.")],
        account_id: Annotated[int, Field(description="ID of the email account to update.")],
        body: Annotated[dict, Field(description=_BODY_DESC)],
    ) -> str:
        """Update an existing mailbox account on an email service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.post(f"/email/{id}/account/{account_id}", json_body=body)
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()
