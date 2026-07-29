import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool()
    async def dynu_add_glue_record_domain(id: int, body: dict) -> str:
        """Add a glue record to a domain.

        API: POST /domain/{id}/glueRecord

        Args:
            id: Required. The id of the domain.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/glueRecord"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_add_name_server_domain(id: int, name_server: str) -> str:
        """Add a name server to a domain.

        API: GET /domain/{id}/nameServer/add

        Args:
            id: Required. The id of the domain.
            name_server: Required. The name server to add to the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/nameServer/add"
        params = {"nameServer": name_server}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_cancel_domain(id: int) -> str:
        """Cancel a domain.

        API: GET /domain/{id}/cancel

        Args:
            id: Required. The id of the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/cancel"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_delete_glue_record_domain(id: int, glue_record_id: int) -> str:
        """Delete a glue record of a domain.

        API: DELETE /domain/{id}/glueRecord/{glueRecordId}

        Args:
            id: Required. The id of the domain.
            glue_record_id: Required. The id of the glue record.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/glueRecord/{glue_record_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_delete_name_server_domain(id: int, name_server: str) -> str:
        """Delete a name server of a domain.

        API: DELETE /domain/{id}/nameServer

        Args:
            id: Required. The id of the domain.
            name_server: Required. The name server to delete for the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/nameServer"
        params = {"nameServer": name_server}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_disable_autorenewal_domain(id: int) -> str:
        """Disable autorenewal for a domain.

        API: GET /domain/{id}/autorenewDisable

        Args:
            id: Required. The id of the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/autorenewDisable"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_enable_autorenewal_domain(id: int) -> str:
        """Enable autorenewal for a domain.

        API: GET /domain/{id}/autorenewEnable

        Args:
            id: Required. The id of the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/autorenewEnable"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

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

    @mcp.tool()
    async def dynu_get_list_glue_records_domain(id: int) -> str:
        """Get a list of glue records for a domain.

        API: GET /domain/{id}/glueRecord

        Args:
            id: Required. The id of the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/glueRecord"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_name_servers_domain(id: int) -> str:
        """Get a list of name servers for a domain.

        API: GET /domain/{id}/nameServer

        Args:
            id: Required. The id of the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/nameServer"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_lock_domain(id: int) -> str:
        """Lock a domain.

        API: GET /domain/{id}/lock

        Args:
            id: Required. The id of the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/lock"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_make_name_server_primary_name_server_domain(id: int, name_server: str) -> str:
        """Make a name server the primary name server of a domain.

        API: GET /domain/{id}/nameServer/primary

        Args:
            id: Required. The id of the domain.
            name_server: Required. The name server to make primary for the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/nameServer/primary"
        params = {"nameServer": name_server}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_unlock_domain(id: int) -> str:
        """Unlock a domain.

        API: GET /domain/{id}/unlock

        Args:
            id: Required. The id of the domain.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/unlock"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_glue_record_domain(id: int, glue_record_id: int, body: dict) -> str:
        """Update a glue record of a domain.

        API: POST /domain/{id}/glueRecord/{glueRecordId}

        Args:
            id: Required. The id of the domain.
            glue_record_id: Required. The id of the glue record.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/domain/{id}/glueRecord/{glue_record_id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
