import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool()
    async def dynu_add_new_blacklist_email_service(id: int, body: dict) -> str:
        """Add a new blacklist for email service.

        API: POST /email/{id}/blacklist

        Args:
            id: Required. The id of the email service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/blacklist"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

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
    async def dynu_add_new_email_alias_email_service(id: int, body: dict) -> str:
        """Add a new email alias for email service.

        API: POST /email/{id}/alias

        Args:
            id: Required. The id of the email service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/alias"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_add_new_email_distribution_list_email_service(id: int, body: dict) -> str:
        """Add a new email distribution list for email service.

        API: POST /email/{id}/distributionlist

        Args:
            id: Required. The id of the email service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/distributionlist"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_add_new_recipient_email_distribution_list(id: int, distribution_list_id: int, body: dict) -> str:
        """Add a new recipient for email distribution list.

        API: POST /email/{id}/distributionlist/{distributionListId}/recipient

        Args:
            id: Required. The id of the email service.
            distribution_list_id: Required. The id of the email distribution list.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/distributionlist/{distribution_list_id}/recipient"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_add_new_whitelist_email_service(id: int, body: dict) -> str:
        """Add a new whitelist for email service.

        API: POST /email/{id}/whitelist

        Args:
            id: Required. The id of the email service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/whitelist"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_details_blacklist_email_service(id: int, blacklist_id: int) -> str:
        """Get details of a blacklist for email service.

        API: GET /email/{id}/blacklist/{blacklistId}

        Args:
            id: Required. The id of the email service.
            blacklist_id: Required. The id of the blacklist for email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/blacklist/{blacklist_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
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
    async def dynu_get_details_email_alias(id: int, alias_id: int) -> str:
        """Get details of the email alias.

        API: GET /email/{id}/alias/{aliasId}

        Args:
            id: Required. The id of the email service.
            alias_id: Required. The id of the email alias.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/alias/{alias_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_details_email_distribution_list(id: int, distribution_list_id: int) -> str:
        """Get details of the email distribution list.

        API: GET /email/{id}/distributionlist/{distributionListId}

        Args:
            id: Required. The id of the email service.
            distribution_list_id: Required. The id of the email distribution list.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/distributionlist/{distribution_list_id}"
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
    async def dynu_get_details_whitelist_email_service(id: int, whitelist_id: int) -> str:
        """Get details of a whitelist for email service.

        API: GET /email/{id}/whitelist/{whitelistId}

        Args:
            id: Required. The id of the email service.
            whitelist_id: Required. The id of the whitelist for email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/whitelist/{whitelist_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_dkim_details_email_service(id: int) -> str:
        """Get DKIM details of the email service.

        API: GET /email/{id}/dkim

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/dkim"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_blacklist(id: int) -> str:
        """Get a list of blacklist.

        API: GET /email/{id}/blacklist

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/blacklist"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_daily_limits_email_service(id: int) -> str:
        """Get a list of daily limits for email service.

        API: GET /email/{id}/dailylimit

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/dailylimit"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_distribution_lists_email_service(id: int) -> str:
        """Get a list of distribution lists for email service.

        API: GET /email/{id}/distributionlist

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/distributionlist"
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
    async def dynu_get_list_email_aliases_email_service(id: int) -> str:
        """Get a list of email aliases for email service.

        API: GET /email/{id}/alias

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/alias"
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
    async def dynu_get_list_messages_in_delivery_queue(id: int) -> str:
        """Get a list of messages in delivery queue.

        API: GET /email/{id}/deliveryQueue

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/deliveryQueue"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_recipients_distribution_list(id: int, distribution_list_id: int) -> str:
        """Get a list of recipients of the distribution list.

        API: GET /email/{id}/distributionlist/{distributionListId}/recipient

        Args:
            id: Required. The id of the email service.
            distribution_list_id: Required. The id of the email distribution list.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/distributionlist/{distribution_list_id}/recipient"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_whitelist(id: int) -> str:
        """Get a list of whitelist.

        API: GET /email/{id}/whitelist

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/whitelist"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_blacklist_email_service(id: int, blacklist_id: int) -> str:
        """Remove a blacklist from email service.

        API: DELETE /email/{id}/blacklist/{blacklistId}

        Args:
            id: Required. The id of the email service.
            blacklist_id: Required. The id of the blacklist for email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/blacklist/{blacklist_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
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
    async def dynu_remove_email_alias_email_service(id: int, alias_id: int) -> str:
        """Remove an email alias from email service.

        API: DELETE /email/{id}/alias/{aliasId}

        Args:
            id: Required. The id of the email service.
            alias_id: Required. The id of the email alias.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/alias/{alias_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_email_distribution_list_email_service(id: int, distribution_list_id: int) -> str:
        """Remove an email distribution list from email service.

        API: DELETE /email/{id}/distributionlist/{distributionListId}

        Args:
            id: Required. The id of the email service.
            distribution_list_id: Required. The id of the email distribution list.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/distributionlist/{distribution_list_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_existing_recipient_email_distribution_list(id: int, distribution_list_id: int, recipient_id: int) -> str:
        """Remove an existing recipient from email distribution list.

        API: DELETE /email/{id}/distributionlist/{distributionListId}/recipient/{recipientId}

        Args:
            id: Required. The id of the email service.
            distribution_list_id: Required. The id of the email distribution list.
            recipient_id: Required. The id of the recipient.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/distributionlist/{distribution_list_id}/recipient/{recipient_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_whitelist_email_service(id: int, whitelist_id: int) -> str:
        """Remove a whitelist from email service.

        API: DELETE /email/{id}/whitelist/{whitelistId}

        Args:
            id: Required. The id of the email service.
            whitelist_id: Required. The id of the whitelist for email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/whitelist/{whitelist_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_this_operation_autogenerates_dkim_details_including_private_key_email_service(id: int) -> str:
        """This operation auto-generates DKIM details including the private key of the email service.

        API: GET /email/{id}/autogeneratedkim

        Args:
            id: Required. The id of the email service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/autogeneratedkim"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_details_existing_blacklist_email_service(id: int, blacklist_id: int, body: dict) -> str:
        """Update details of an existing blacklist for email service.

        API: POST /email/{id}/blacklist/{blacklistId}

        Args:
            id: Required. The id of the email service.
            blacklist_id: Required. The id of the blacklist for email service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/blacklist/{blacklist_id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_details_existing_whitelist_email_service(id: int, whitelist_id: int, body: dict) -> str:
        """Update details of an existing whitelist for email service.

        API: POST /email/{id}/whitelist/{whitelistId}

        Args:
            id: Required. The id of the email service.
            whitelist_id: Required. The id of the whitelist for email service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/whitelist/{whitelist_id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_dkim_details_email_service(id: int, body: dict) -> str:
        """Update DKIM details for the email service.

        API: POST /email/{id}/dkim

        Args:
            id: Required. The id of the email service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/dkim"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_email_service(id: int, body: dict) -> str:
        """Update an email service.

        API: POST /email/{id}

        Args:
            id: Required. The id of the email service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
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

    @mcp.tool()
    async def dynu_update_existing_email_alias_email_service(id: int, alias_id: int, body: dict) -> str:
        """Update an existing email alias for email service.

        API: POST /email/{id}/alias/{aliasId}

        Args:
            id: Required. The id of the email service.
            alias_id: Required. The id of the email alias.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/alias/{alias_id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_existing_email_distribution_list_email_service(id: int, distribution_list_id: int, body: dict) -> str:
        """Update an existing email distribution list for email service.

        API: POST /email/{id}/distributionlist/{distributionListId}

        Args:
            id: Required. The id of the email service.
            distribution_list_id: Required. The id of the email distribution list.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/email/{id}/distributionlist/{distribution_list_id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
