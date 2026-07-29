# dynu-mcp

MCP server for **Dynu** — a Dynamic DNS, domain registration, email
hosting, and cloud compute (VPS) provider. Exposes the full public Dynu
REST API v2 as MCP tools.

## Overview

- Stateless HTTP service. No credentials are ever persisted — each request
  supplies its own API key via a header, used only for the lifetime of
  that single request.
- Supports concurrent requests; per-request credential isolation is done
  via Python `contextvars`, not a global/shared client instance.
- Entry points: `POST /mcp` (MCP protocol) and `GET /health` (health check).
- Default port: `8080` (configurable via `MCP_HTTP_PORT`).

## Scope

**117 tools**, one per operation in Dynu's official OpenAPI 3.0 spec
(`Dynu.API.OAS.zip`, downloaded from https://www.dynu.com/Support/API),
across 6 categories: `dns` (30), `email` (36), `compute` (27), `domain`
(15), `monitor` (7), `ping` (2). Per explicit user decision, this covers
the **full public API including write operations** (POST/DELETE — adding,
updating, and removing DNS records, domains, email accounts, and even
VPS compute instances), not just the 66 `GET` read methods. MSPbots
itself only calls 1 endpoint (`GET /dns`) — see **Known Gaps** for
important caveats about the higher-stakes `compute`/`domain` categories.

## Authentication

Dynu authenticates with a single static **API key** (found in the API
Credentials area of the Dynu control panel). MSPbots' own integration
convention sends this key as the raw value of the `API-Key` header, and
this server forwards it exactly that way.

### HEADER 授权参数说明

| Header | 类型 | 是否必填 | 默认值 | 枚举值 | 字段描述 | Example |
|---|---|---|---|---|---|---|
| `X-Dynu-Api-Key` | string | 是 | 无 | 无 | Dynu 静态 API Key，原样转发为上游 `API-Key` 请求头 | `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6` |

Missing the header returns `401`:
```json
{
  "error": "Missing credentials",
  "message": "This server requires the X-Dynu-Api-Key header",
  "required_headers": ["X-Dynu-Api-Key"],
  "optional_headers": []
}
```

## Environment Variables

| Variable | 类型 | 是否必填 | 默认值 | 说明 |
|---|---|---|---|---|
| `MCP_HTTP_PORT` | int | 否 | `8080` | HTTP 监听端口 |
| `MCP_HTTP_HOST` | string | 否 | `0.0.0.0` | HTTP 监听地址 |
| `DYNU_BASE_URL` | string | 否 | `https://api.dynu.com/v2` | Dynu API 基础 URL |

## MCP Endpoint

- `POST /mcp` — MCP protocol (streamable HTTP transport)
- `GET /health` — health check, returns `{"status": "ok", "service": "dynu-mcp", "transport": "http"}`

## Tool List

Tool names are derived from each operation's own summary in the vendor's
OpenAPI spec (e.g. "Get a list of domains for DNS service" →
`dynu_get_list_domains_dns_service`); the one naming collision (both
`GET /ping` and `POST /ping` share an identical summary) is disambiguated
with a `_get`/`_post` suffix. `body` parameters for POST operations are
accepted as a generic `dict` — see the vendor's OpenAPI spec's Models
section (linked below) for the exact field names/types of each resource.

| Category | Tool | 功能 | 方法+路径 | 参数 |
|---|---|---|---|---|
| email | `dynu_add_new_blacklist_email_service` | Add a new blacklist for email service. | POST /email/{id}/blacklist | id(必填), body(必填,dict) |
| email | `dynu_add_new_email_account_email_service` | Add a new email account for email service. | POST /email/{id}/account | id(必填), body(必填,dict) |
| email | `dynu_add_new_email_alias_email_service` | Add a new email alias for email service. | POST /email/{id}/alias | id(必填), body(必填,dict) |
| email | `dynu_add_new_email_distribution_list_email_service` | Add a new email distribution list for email service. | POST /email/{id}/distributionlist | id(必填), body(必填,dict) |
| email | `dynu_add_new_recipient_email_distribution_list` | Add a new recipient for email distribution list. | POST /email/{id}/distributionlist/{distributionListId}/recipient | id(必填), distribution_list_id(必填), body(必填,dict) |
| email | `dynu_add_new_whitelist_email_service` | Add a new whitelist for email service. | POST /email/{id}/whitelist | id(必填), body(必填,dict) |
| email | `dynu_get_details_blacklist_email_service` | Get details of a blacklist for email service. | GET /email/{id}/blacklist/{blacklistId} | id(必填), blacklist_id(必填) |
| email | `dynu_get_details_email_account` | Get details of the email account. | GET /email/{id}/account/{accountId} | id(必填), account_id(必填) |
| email | `dynu_get_details_email_alias` | Get details of the email alias. | GET /email/{id}/alias/{aliasId} | id(必填), alias_id(必填) |
| email | `dynu_get_details_email_distribution_list` | Get details of the email distribution list. | GET /email/{id}/distributionlist/{distributionListId} | id(必填), distribution_list_id(必填) |
| email | `dynu_get_details_email_service` | Get details of an email service. | GET /email/{id} | id(必填) |
| email | `dynu_get_details_whitelist_email_service` | Get details of a whitelist for email service. | GET /email/{id}/whitelist/{whitelistId} | id(必填), whitelist_id(必填) |
| email | `dynu_get_dkim_details_email_service` | Get DKIM details of the email service. | GET /email/{id}/dkim | id(必填) |
| email | `dynu_get_list_blacklist` | Get a list of blacklist. | GET /email/{id}/blacklist | id(必填) |
| email | `dynu_get_list_daily_limits_email_service` | Get a list of daily limits for email service. | GET /email/{id}/dailylimit | id(必填) |
| email | `dynu_get_list_distribution_lists_email_service` | Get a list of distribution lists for email service. | GET /email/{id}/distributionlist | id(必填) |
| email | `dynu_get_list_email_accounts_email_service` | Get a list of email accounts for email service. | GET /email/{id}/account | id(必填) |
| email | `dynu_get_list_email_aliases_email_service` | Get a list of email aliases for email service. | GET /email/{id}/alias | id(必填) |
| email | `dynu_get_list_email_services` | Get a list of email services. | GET /email | 无 |
| email | `dynu_get_list_messages_in_delivery_queue` | Get a list of messages in delivery queue. | GET /email/{id}/deliveryQueue | id(必填) |
| email | `dynu_get_list_recipients_distribution_list` | Get a list of recipients of the distribution list. | GET /email/{id}/distributionlist/{distributionListId}/recipient | id(必填), distribution_list_id(必填) |
| email | `dynu_get_list_whitelist` | Get a list of whitelist. | GET /email/{id}/whitelist | id(必填) |
| email | `dynu_remove_blacklist_email_service` | Remove a blacklist from email service. | DELETE /email/{id}/blacklist/{blacklistId} | id(必填), blacklist_id(必填) |
| email | `dynu_remove_email_account_email_service` | Remove an email account from email service. | DELETE /email/{id}/account/{accountId} | id(必填), account_id(必填) |
| email | `dynu_remove_email_alias_email_service` | Remove an email alias from email service. | DELETE /email/{id}/alias/{aliasId} | id(必填), alias_id(必填) |
| email | `dynu_remove_email_distribution_list_email_service` | Remove an email distribution list from email service. | DELETE /email/{id}/distributionlist/{distributionListId} | id(必填), distribution_list_id(必填) |
| email | `dynu_remove_existing_recipient_email_distribution_list` | Remove an existing recipient from email distribution list. | DELETE /email/{id}/distributionlist/{distributionListId}/recipient/{recipientId} | id(必填), distribution_list_id(必填), recipient_id(必填) |
| email | `dynu_remove_whitelist_email_service` | Remove a whitelist from email service. | DELETE /email/{id}/whitelist/{whitelistId} | id(必填), whitelist_id(必填) |
| email | `dynu_this_operation_autogenerates_dkim_details_including_private_key_email_service` | This operation auto-generates DKIM details including the private key of the email service. | GET /email/{id}/autogeneratedkim | id(必填) |
| email | `dynu_update_details_existing_blacklist_email_service` | Update details of an existing blacklist for email service. | POST /email/{id}/blacklist/{blacklistId} | id(必填), blacklist_id(必填), body(必填,dict) |
| email | `dynu_update_details_existing_whitelist_email_service` | Update details of an existing whitelist for email service. | POST /email/{id}/whitelist/{whitelistId} | id(必填), whitelist_id(必填), body(必填,dict) |
| email | `dynu_update_dkim_details_email_service` | Update DKIM details for the email service. | POST /email/{id}/dkim | id(必填), body(必填,dict) |
| email | `dynu_update_email_service` | Update an email service. | POST /email/{id} | id(必填), body(必填,dict) |
| email | `dynu_update_existing_email_account_email_service` | Update an existing email account for email service. | POST /email/{id}/account/{accountId} | id(必填), account_id(必填), body(必填,dict) |
| email | `dynu_update_existing_email_alias_email_service` | Update an existing email alias for email service. | POST /email/{id}/alias/{aliasId} | id(必填), alias_id(必填), body(必填,dict) |
| email | `dynu_update_existing_email_distribution_list_email_service` | Update an existing email distribution list for email service. | POST /email/{id}/distributionlist/{distributionListId} | id(必填), distribution_list_id(必填), body(必填,dict) |
| dns | `dynu_add_new_dns_record_dns_service` | Add a new DNS record for DNS service. | POST /dns/{id}/record | id(必填), body(必填,dict) |
| dns | `dynu_add_new_dns_service` | Add a new DNS service. | POST /dns | body(必填,dict) |
| dns | `dynu_add_new_group` | Add a new group. | POST /dns/group | body(必填,dict) |
| dns | `dynu_add_new_web_redirect` | Add a new web redirect. | POST /dns/{id}/webredirect | id(必填), body(必填,dict) |
| dns | `dynu_disable_dns_record_dns_service` | Disable the DNS record for DNS service. | GET /dns/{id}/record/{dnsRecordId}/disable | id(必填), dns_record_id(必填) |
| dns | `dynu_disable_dnssec_dns_service` | Disable DNSSEC for DNS service. | GET /dns/{id}/dnssec/disable | id(必填) |
| dns | `dynu_ds_record_dnssec_dns_service` | DS record of DNSSEC for DNS service. | GET /dns/{id}/dnssec | id(必填) |
| dns | `dynu_enable_dns_record_dns_service` | Enable the DNS record for DNS service. | GET /dns/{id}/record/{dnsRecordId}/enable | id(必填), dns_record_id(必填) |
| dns | `dynu_enable_dnssec_dns_service` | Enable DNSSEC for DNS service. | GET /dns/{id}/dnssec/enable | id(必填) |
| dns | `dynu_get_details_dns_record_dns_service` | Get details of a DNS record for DNS service. | GET /dns/{id}/record/{dnsRecordId} | id(必填), dns_record_id(必填) |
| dns | `dynu_get_details_domain_dns_service` | Get details of a domain for DNS service. | GET /dns/{id} | id(必填) |
| dns | `dynu_get_details_web_redirect` | Get details of the web redirect. | GET /dns/{id}/webRedirect/{webRedirectId} | id(必填), web_redirect_id(必填) |
| dns | `dynu_get_dns_records_based_hostname_and_resource_record_type` | Get DNS records based on a hostname and resource record type. | GET /dns/record/{hostname} | hostname(必填), record_type(必填) |
| dns | `dynu_get_list_dns_records_dns_service` | Get a list of DNS records for DNS service. | GET /dns/{id}/record | id(必填) |
| dns | `dynu_get_list_domains_dns_service` | Get a list of domains for DNS service. | GET /dns | 无 |
| dns | `dynu_get_list_groups_which_hosts_are_assigned` | Get a list of groups to which hosts are assigned to. | GET /dns/group | 无 |
| dns | `dynu_get_list_ip_address_updates` | Get a list of IP address updates. | GET /dns/ipUpdateHistory | 无 |
| dns | `dynu_get_list_top_levels` | Get a list of top levels. | GET /dns/toplevel | 无 |
| dns | `dynu_get_list_web_redirects` | Get a list of web redirects. | GET /dns/{id}/webredirect | id(必填) |
| dns | `dynu_get_root_domain_name_based_hostname` | Get the root domain name based on a hostname. | GET /dns/getroot/{hostname} | hostname(必填) |
| dns | `dynu_limits_associated_dns_records` | Limits associated with DNS records. | GET /dns/{id}/limit | id(必填) |
| dns | `dynu_limits_associated_hostnames` | Limits associated with hostnames. | GET /dns/limit | 无 |
| dns | `dynu_remove_dns_record_dns_service` | Remove a DNS record from DNS service. | DELETE /dns/{id}/record/{dnsRecordId} | id(必填), dns_record_id(必填) |
| dns | `dynu_remove_domain_dns_service` | Remove domain from DNS service. | DELETE /dns/{id} | id(必填) |
| dns | `dynu_remove_group` | Remove a group. | DELETE /dns/group/{id} | id(必填) |
| dns | `dynu_remove_web_redirect` | Remove a web redirect. | DELETE /dns/{id}/webRedirect/{webRedirectId} | id(必填), web_redirect_id(必填) |
| dns | `dynu_update_existing_dns_record_dns_service` | Update an existing DNS record for DNS service. | POST /dns/{id}/record/{dnsRecordId} | id(必填), dns_record_id(必填), body(必填,dict) |
| dns | `dynu_update_existing_dns_service` | Update an existing DNS service. | POST /dns/{id} | id(必填), body(必填,dict) |
| dns | `dynu_update_existing_group` | Update an existing group. | POST /dns/group/{id} | id(必填), body(必填,dict) |
| dns | `dynu_update_existing_web_redirect` | Update an existing web redirect. | POST /dns/{id}/webRedirect/{webRedirectId} | id(必填), web_redirect_id(必填), body(必填,dict) |
| compute | `dynu_change_operating_system_password` | Change the operating system password. | POST /compute/instance/{id}/password | id(必填), body(必填,dict) |
| compute | `dynu_change_vnc_password` | Change the VNC password. | POST /compute/instance/{id}/vnc | id(必填), body(必填,dict) |
| compute | `dynu_create_manual_backup` | Create a manual backup. | POST /compute/instance/{id}/backup | id(必填) |
| compute | `dynu_create_or_update_reverse_dns_mapping` | Create or update a reverse DNS mapping. | POST /compute/instance/{id}/reversedns | id(必填), body(必填,dict) |
| compute | `dynu_create_snapshot` | Create a snapshot. | POST /compute/instance/{id}/snapshot | id(必填) |
| compute | `dynu_get_instance` | Get an instance. | GET /compute/instance/{id} | id(必填) |
| compute | `dynu_get_list_active_tasks` | Get a list of active tasks. | GET /compute/instance/{id}/task | id(必填) |
| compute | `dynu_get_list_backups` | Get a list of backups. | GET /compute/instance/{id}/backup | id(必填) |
| compute | `dynu_get_list_instances` | Get a list of instances. | GET /compute/instance | 无 |
| compute | `dynu_get_list_operating_systems_available_reinstall` | Get a list of operating systems available for reinstall. | GET /compute/os | 无 |
| compute | `dynu_get_list_snapshots` | Get a list of snapshots. | GET /compute/instance/{id}/snapshot | id(必填) |
| compute | `dynu_get_network_settings` | Get network settings. | GET /compute/instance/{id}/network | id(必填) |
| compute | `dynu_get_reverse_dns_mappings` | Get reverse DNS mappings. | GET /compute/instance/{id}/reversedns | id(必填) |
| compute | `dynu_get_vnc_connection_details` | Get VNC connection details. | GET /compute/instance/{id}/vnc | id(必填) |
| compute | `dynu_mount_iso_image` | Mount an ISO image. | POST /compute/instance/{id}/mountiso | id(必填), body(必填,dict) |
| compute | `dynu_reinstall_operating_system` | Reinstall the operating system. | POST /compute/instance/{id}/reinstall | id(必填), body(必填,dict) |
| compute | `dynu_remove_all_snapshots` | Remove all snapshots. | DELETE /compute/instance/{id}/snapshot | id(必填) |
| compute | `dynu_remove_backup` | Remove a backup. | DELETE /compute/instance/{id}/backup/{backupId} | id(必填), backup_id(必填) |
| compute | `dynu_remove_ipv6_reverse_dns_mapping` | Remove an IPv6 reverse DNS mapping. | DELETE /compute/instance/{id}/reversedns/{ptrRecordId} | id(必填), ptr_record_id(必填) |
| compute | `dynu_remove_snapshot` | Remove a snapshot. | DELETE /compute/instance/{id}/snapshot/{snapshotId} | id(必填), snapshot_id(必填) |
| compute | `dynu_restart_instance` | Restart an instance. | GET /compute/instance/{id}/restart | id(必填) |
| compute | `dynu_restore_backup` | Restore a backup. | GET /compute/instance/{id}/backup/{backupId}/restore | id(必填), backup_id(必填) |
| compute | `dynu_restore_snapshot` | Restore a snapshot. | GET /compute/instance/{id}/snapshot/{snapshotId}/restore | id(必填), snapshot_id(必填) |
| compute | `dynu_start_instance` | Start an instance. | GET /compute/instance/{id}/start | id(必填) |
| compute | `dynu_stop_suspend_instance` | Stop (suspend) an instance. | GET /compute/instance/{id}/stop | id(必填) |
| compute | `dynu_unmount_iso_image` | Unmount the ISO image. | POST /compute/instance/{id}/unmountiso | id(必填), body(必填,dict) |
| compute | `dynu_update_instance_label_or_cpu_emulation_mode` | Update an instance label or CPU emulation mode. | POST /compute/instance/{id} | id(必填), body(必填,dict) |
| domain | `dynu_add_glue_record_domain` | Add a glue record to a domain. | POST /domain/{id}/glueRecord | id(必填), body(必填,dict) |
| domain | `dynu_add_name_server_domain` | Add a name server to a domain. | GET /domain/{id}/nameServer/add | id(必填), name_server(必填) |
| domain | `dynu_cancel_domain` | Cancel a domain. | GET /domain/{id}/cancel | id(必填) |
| domain | `dynu_delete_glue_record_domain` | Delete a glue record of a domain. | DELETE /domain/{id}/glueRecord/{glueRecordId} | id(必填), glue_record_id(必填) |
| domain | `dynu_delete_name_server_domain` | Delete a name server of a domain. | DELETE /domain/{id}/nameServer | id(必填), name_server(必填) |
| domain | `dynu_disable_autorenewal_domain` | Disable autorenewal for a domain. | GET /domain/{id}/autorenewDisable | id(必填) |
| domain | `dynu_enable_autorenewal_domain` | Enable autorenewal for a domain. | GET /domain/{id}/autorenewEnable | id(必填) |
| domain | `dynu_get_details_domain_registration_domain` | Get details of a domain registration domain. | GET /domain/{id} | id(必填) |
| domain | `dynu_get_list_domains_domain_registration_service` | Get a list of domains for domain registration service. | GET /domain | 无 |
| domain | `dynu_get_list_glue_records_domain` | Get a list of glue records for a domain. | GET /domain/{id}/glueRecord | id(必填) |
| domain | `dynu_get_list_name_servers_domain` | Get a list of name servers for a domain. | GET /domain/{id}/nameServer | id(必填) |
| domain | `dynu_lock_domain` | Lock a domain. | GET /domain/{id}/lock | id(必填) |
| domain | `dynu_make_name_server_primary_name_server_domain` | Make a name server the primary name server of a domain. | GET /domain/{id}/nameServer/primary | id(必填), name_server(必填) |
| domain | `dynu_unlock_domain` | Unlock a domain. | GET /domain/{id}/unlock | id(必填) |
| domain | `dynu_update_glue_record_domain` | Update a glue record of a domain. | POST /domain/{id}/glueRecord/{glueRecordId} | id(必填), glue_record_id(必填), body(必填,dict) |
| monitor | `dynu_add_new_monitor` | Add a new monitor. | POST /monitor | body(必填,dict) |
| monitor | `dynu_delete_monitor` | Delete a monitor. | DELETE /monitor/{id} | id(必填) |
| monitor | `dynu_get_details_monitor` | Get details of a monitor. | GET /monitor/{id} | id(必填) |
| monitor | `dynu_get_list_monitors` | Get a list of monitors. | GET /monitor | 无 |
| monitor | `dynu_limits_associated_monitoring` | Limits associated with monitoring. | GET /monitor/limit | 无 |
| monitor | `dynu_pause_monitor` | Pause a monitor. | GET /monitor/{id}/pause | id(必填) |
| monitor | `dynu_unpause_monitor` | Unpause a monitor. | GET /monitor/{id}/unpause | id(必填) |
| ping | `dynu_ping_api_server_obtain_pong_response_get` | Ping the API server to obtain the pong response. | GET /ping | message(必填) |
| ping | `dynu_ping_api_server_obtain_pong_response_post` | Ping the API server to obtain the pong response. | POST /ping | body(必填,dict) |

## 测试示例

```bash
# Health check
curl -s http://localhost:8080/health

# Call a tool via the MCP protocol (streamable HTTP) — requires an
# initialize handshake first per the MCP spec; abbreviated example below
# shows the tool-call request body only:
curl -s -X POST http://localhost:8080/mcp   -H "X-Dynu-Api-Key: <your-dynu-api-key>"   -H "Content-Type: application/json"   -H "Accept: application/json, text/event-stream"   -H "mcp-session-id: <session-id-from-initialize>"   -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "dynu_get_list_domains_dns_service",
      "arguments": {}
    }
  }'
```

**Live-verified** (2026-07-29): `dynu_get_list_domains_dns_service` (the
same endpoint MSPbots itself calls, zero parameters) was called end-to-end
through this running server with a real API key and returned real DNS
domain records for the account.

## API Reference

- Overview: https://www.dynu.com/Support/API
- Official OpenAPI 3.0 spec (Swagger): https://www.dynu.com/files/dynu.api/Dynu.API.OAS.zip

## Known Gaps

- **Full API coverage was an explicit user decision**, matching the pattern
  used for other large public APIs in this program (e.g. ConnectSecure,
  Cove Data Protection). Unlike those, Dynu's `compute` category manages
  **real VPS instances** (start/stop/restart/reinstall OS/change
  password/mount ISO) and `domain` includes registrar-level actions
  (lock/unlock/cancel a domain, manage nameservers) — these are
  meaningfully higher-stakes than DNS record management. Treat any tool
  whose name starts with `dynu_reinstall_`, `dynu_stop_`, `dynu_cancel_`,
  `dynu_change_operating_system_password_`, or similar as **destructive/
  irreversible** and confirm with a human before invoking.
- **`body` parameters are untyped (`dict`)** rather than fully modeled —
  the OpenAPI spec's Models section defines the exact schema per resource
  (e.g. `DNS.dnsRecordA`, `Compute.instanceUpdate`), but reproducing all of
  them as typed Python parameters was out of scope for a 117-tool
  generation. Callers should shape the `body` dict per the linked spec.
- Only `dynu_get_list_domains_dns_service` (MSPbots' own endpoint) was
  live-verified with real account data. The remaining 116 tools are
  structurally correct (schema validated, MCP-protocol `tools/list`
  confirmed) but not individually smoke-tested — most are write/destructive
  operations that would create, modify, or delete real DNS records,
  domains, email accounts, or VPS instances, so they weren't exercised
  against the live test account.
