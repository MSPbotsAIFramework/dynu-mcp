import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool()
    async def dynu_add_new_email_account_email_service(id: int, body: dict) -> str:
        """Add a new email account for email service.

        API: POST /email/{id}/account

        Args:
            id: Required. The id of the email service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/account"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_details_email_account(id: int, account_id: int) -> str:
        """Get details of the email account.

        API: GET /email/{id}/account/{accountId}

        Args:
            id: Required. The id of the email service.
            account_id: Required. The id of the email account.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/account/{account_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_details_email_service(id: int) -> str:
        """Get details of an email service.

        API: GET /email/{id}

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_email_accounts_email_service(id: int) -> str:
        """Get a list of email accounts for email service.

        API: GET /email/{id}/account

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/account"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_email_services() -> str:
        """Get a list of email services.

        API: GET /email

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/email", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_email_account_email_service(id: int, account_id: int) -> str:
        """Remove an email account from email service.

        API: DELETE /email/{id}/account/{accountId}

        Args:
            id: Required. The id of the email service.
            account_id: Required. The id of the email account.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/account/{account_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_existing_email_account_email_service(id: int, account_id: int, body: dict) -> str:
        """Update an existing email account for email service.

        API: POST /email/{id}/account/{accountId}

        Args:
            id: Required. The id of the email service.
            account_id: Required. The id of the email account.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/account/{account_id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
