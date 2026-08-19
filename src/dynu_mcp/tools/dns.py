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
    async def dynu_add_new_dns_record_dns_service(
        id: Annotated[int, Field(description="ID of the domain for the DNS service.")],
        body: Annotated[dict, Field(description=_BODY_DESC)],
    ) -> str:
        """Add a new DNS record to a domain's DNS service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.post(f"/dns/{id}/record", json_body=body)
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(idempotentHint=False))
    async def dynu_add_new_dns_service(
        body: Annotated[dict, Field(description=_BODY_DESC)],
    ) -> str:
        """Add a new DNS service for a domain."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.post("/dns", json_body=body)
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_details_dns_record_dns_service(
        id: Annotated[int, Field(description="ID of the domain for the DNS service.")],
        dns_record_id: Annotated[int, Field(description="ID of the DNS record.")],
    ) -> str:
        """Get details of a single DNS record on a domain's DNS service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/dns/{id}/record/{dns_record_id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_details_domain_dns_service(
        id: Annotated[int, Field(description="ID of the domain for the DNS service.")],
    ) -> str:
        """Get details of a domain's DNS service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/dns/{id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_list_dns_records_dns_service(
        id: Annotated[int, Field(description="ID of the domain for the DNS service.")],
    ) -> str:
        """List all DNS records on a domain's DNS service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get(f"/dns/{id}/record")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def dynu_get_list_domains_dns_service() -> str:
        """List all domains configured for the DNS service on the account."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.get("/dns")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(destructiveHint=True, idempotentHint=True))
    async def dynu_remove_dns_record_dns_service(
        id: Annotated[int, Field(description="ID of the domain for the DNS service.")],
        dns_record_id: Annotated[int, Field(description="ID of the DNS record to remove.")],
    ) -> str:
        """Remove a DNS record from a domain's DNS service. Irreversible."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.delete(f"/dns/{id}/record/{dns_record_id}")
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(idempotentHint=True))
    async def dynu_update_existing_dns_record_dns_service(
        id: Annotated[int, Field(description="ID of the domain for the DNS service.")],
        dns_record_id: Annotated[int, Field(description="ID of the DNS record to update.")],
        body: Annotated[dict, Field(description=_BODY_DESC)],
    ) -> str:
        """Update an existing DNS record on a domain's DNS service."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.post(f"/dns/{id}/record/{dns_record_id}", json_body=body)
            return dump_json_capped(result)
        except DynuError as e:
            return e.to_envelope()
