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
    async def dynu_add_new_group(body: dict) -> str:
        """Add a new group.

        API: POST /dns/group

        Args:
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/dns/group", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_add_new_web_redirect(id: int, body: dict) -> str:
        """Add a new web redirect.

        API: POST /dns/{id}/webredirect

        Args:
            id: Required. The id of the domain for DNS service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/webredirect"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_disable_dns_record_dns_service(id: int, dns_record_id: int) -> str:
        """Disable the DNS record for DNS service.

        API: GET /dns/{id}/record/{dnsRecordId}/disable

        Args:
            id: Required. The id of the domain for DNS service.
            dns_record_id: Required. The id of the DNS record for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/record/{dns_record_id}/disable"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_disable_dnssec_dns_service(id: int) -> str:
        """Disable DNSSEC for DNS service.

        API: GET /dns/{id}/dnssec/disable

        Args:
            id: Required. The id of the domain for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/dnssec/disable"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_ds_record_dnssec_dns_service(id: int) -> str:
        """DS record of DNSSEC for DNS service.

        API: GET /dns/{id}/dnssec

        Args:
            id: Required. The id of the domain for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/dnssec"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_enable_dns_record_dns_service(id: int, dns_record_id: int) -> str:
        """Enable the DNS record for DNS service.

        API: GET /dns/{id}/record/{dnsRecordId}/enable

        Args:
            id: Required. The id of the domain for DNS service.
            dns_record_id: Required. The id of the DNS record for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/record/{dns_record_id}/enable"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_enable_dnssec_dns_service(id: int) -> str:
        """Enable DNSSEC for DNS service.

        API: GET /dns/{id}/dnssec/enable

        Args:
            id: Required. The id of the domain for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/dnssec/enable"
        params = {}
        try:
            result = await client.get(path, params=params)
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
    async def dynu_get_details_web_redirect(id: int, web_redirect_id: int) -> str:
        """Get details of the web redirect.

        API: GET /dns/{id}/webRedirect/{webRedirectId}

        Args:
            id: Required. The id of the domain for DNS service.
            web_redirect_id: Required. The id of the web redirect.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/webRedirect/{web_redirect_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_dns_records_based_hostname_and_resource_record_type(hostname: str, record_type: str) -> str:
        """Get DNS records based on a hostname and resource record type.

        API: GET /dns/record/{hostname}

        Args:
            hostname: Required. The hostname of the DNS records.
            record_type: Required. The record type of DNS records. One of: ['A', 'AAAA', 'AFSDB', 'CAA', 'CERT', 'CNAME', 'DHCID', 'DNAME', 'HINFO', 'HTTPS', 'KEY', 'LOC', 'MX', 'NAPTR', 'NS', 'OPENPGPKEY', 'PTR', 'PF', 'RP', 'SMIMEA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT', 'UF', 'URI'].
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/record/{hostname}"
        params = {"recordType": record_type}
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
    async def dynu_get_list_groups_which_hosts_are_assigned() -> str:
        """Get a list of groups to which hosts are assigned to.

        API: GET /dns/group

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/dns/group", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_ip_address_updates() -> str:
        """Get a list of IP address updates.

        API: GET /dns/ipUpdateHistory

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/dns/ipUpdateHistory", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_top_levels() -> str:
        """Get a list of top levels.

        API: GET /dns/toplevel

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/dns/toplevel", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_web_redirects(id: int) -> str:
        """Get a list of web redirects.

        API: GET /dns/{id}/webredirect

        Args:
            id: Required. The id of the domain for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/webredirect"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_root_domain_name_based_hostname(hostname: str) -> str:
        """Get the root domain name based on a hostname.

        API: GET /dns/getroot/{hostname}

        Args:
            hostname: Required. The child hostname of the domain for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/getroot/{hostname}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_limits_associated_dns_records(id: int) -> str:
        """Limits associated with DNS records.

        API: GET /dns/{id}/limit

        Args:
            id: Required. The id of the domain for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/limit"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_limits_associated_hostnames() -> str:
        """Limits associated with hostnames.

        API: GET /dns/limit

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/dns/limit", params=params)
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
    async def dynu_remove_domain_dns_service(id: int) -> str:
        """Remove domain from DNS service.

        API: DELETE /dns/{id}

        Args:
            id: Required. The id of the domain for DNS service.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_group(id: int) -> str:
        """Remove a group.

        API: DELETE /dns/group/{id}

        Args:
            id: Required. The id of the group.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/group/{id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_web_redirect(id: int, web_redirect_id: int) -> str:
        """Remove a web redirect.

        API: DELETE /dns/{id}/webRedirect/{webRedirectId}

        Args:
            id: Required. The id of the domain for DNS service.
            web_redirect_id: Required. The id of the web redirect.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/webRedirect/{web_redirect_id}"
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

    @mcp.tool()
    async def dynu_update_existing_dns_service(id: int, body: dict) -> str:
        """Update an existing DNS service.

        API: POST /dns/{id}

        Args:
            id: Required. The id of the domain for DNS service.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_existing_group(id: int, body: dict) -> str:
        """Update an existing group.

        API: POST /dns/group/{id}

        Args:
            id: Required. The id of the group.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/group/{id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_existing_web_redirect(id: int, web_redirect_id: int, body: dict) -> str:
        """Update an existing web redirect.

        API: POST /dns/{id}/webRedirect/{webRedirectId}

        Args:
            id: Required. The id of the domain for DNS service.
            web_redirect_id: Required. The id of the web redirect.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/dns/{id}/webRedirect/{web_redirect_id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
