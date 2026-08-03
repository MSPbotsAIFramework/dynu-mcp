import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool()
    async def dynu_add_new_dns_record_dns_service(id: int, body: dict) -> str:
        """Add a new DNS record for DNS service.

        API: POST /dns/{id}/record

        Args:
            id: Required. The id of the domain for DNS service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/record"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_add_new_dns_service(body: dict) -> str:
        """Add a new DNS service.

        API: POST /dns

        Args:
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/dns", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_details_dns_record_dns_service(id: int, dns_record_id: int) -> str:
        """Get details of a DNS record for DNS service.

        API: GET /dns/{id}/record/{dnsRecordId}

        Args:
            id: Required. The id of the domain for DNS service.
            dns_record_id: Required. The id of the DNS record for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/record/{dns_record_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_details_domain_dns_service(id: int) -> str:
        """Get details of a domain for DNS service.

        API: GET /dns/{id}

        Args:
            id: Required. The id of the domain for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_dns_records_dns_service(id: int) -> str:
        """Get a list of DNS records for DNS service.

        API: GET /dns/{id}/record

        Args:
            id: Required. The id of the domain for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/record"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_domains_dns_service() -> str:
        """Get a list of domains for DNS service.

        API: GET /dns

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/dns", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_dns_record_dns_service(id: int, dns_record_id: int) -> str:
        """Remove a DNS record from DNS service.

        API: DELETE /dns/{id}/record/{dnsRecordId}

        Args:
            id: Required. The id of the domain for DNS service.
            dns_record_id: Required. The id of the DNS record for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/record/{dns_record_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_existing_dns_record_dns_service(id: int, dns_record_id: int, body: dict) -> str:
        """Update an existing DNS record for DNS service.

        API: POST /dns/{id}/record/{dnsRecordId}

        Args:
            id: Required. The id of the domain for DNS service.
            dns_record_id: Required. The id of the DNS record for DNS service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/record/{dns_record_id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
