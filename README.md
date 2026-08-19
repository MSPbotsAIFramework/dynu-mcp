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

**30 tools**, trimmed down from an initial 117-tool build covering Dynu's
full OpenAPI 3.0 spec. The platform this MCP runs behind aggregates every
enabled vendor MCP's tools into a single Gemini/Vertex model call, which
caps out at 512 total function declarations — with 50+ vendor MCPs
registered, each one needs to stay lean. Kept, across the same 6
categories: `dns` (8 — MSPbots' real `GET /dns` endpoint plus core
record/service CRUD), `email` (7 — service list/detail, account
create/read/update/delete), `compute` (4 — instance list/detail/start/stop),
`domain` (2 — list/detail), `monitor` (7, full category), `ping` (2, full
category). Cut entirely: domain registration administration (glue
records, name servers, auto-renewal, lock/unlock), email's
blacklist/whitelist/alias/distribution-list/DKIM management, and compute's
backup/snapshot/VNC/reinstall operations — see **Known Gaps**. MSPbots
itself only calls 1 endpoint (`GET /dns`), which is kept.

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
- `GET /health` — health check, returns `{"status": "ok"}` (pure local liveness probe, does not depend on the Dynu API)

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
| dns | `dynu_add_new_dns_record_dns_service` | Add a new DNS record for DNS service. | POST /dns/{id}/record | id(必填), body(必填,dict) |
| dns | `dynu_add_new_dns_service` | Add a new DNS service. | POST /dns | body(必填,dict) |
| dns | `dynu_get_details_dns_record_dns_service` | Get details of a DNS record for DNS service. | GET /dns/{id}/record/{dnsRecordId} | id(必填), dns_record_id(必填) |
| dns | `dynu_get_details_domain_dns_service` | Get details of a domain for DNS service. | GET /dns/{id} | id(必填) |
| dns | `dynu_get_list_dns_records_dns_service` | Get a list of DNS records for DNS service. | GET /dns/{id}/record | id(必填) |
| dns | `dynu_get_list_domains_dns_service` | Get a list of domains for DNS service. | GET /dns |  |
| dns | `dynu_remove_dns_record_dns_service` | Remove a DNS record from DNS service. | DELETE /dns/{id}/record/{dnsRecordId} | id(必填), dns_record_id(必填) |
| dns | `dynu_update_existing_dns_record_dns_service` | Update an existing DNS record for DNS service. | POST /dns/{id}/record/{dnsRecordId} | id(必填), dns_record_id(必填), body(必填,dict) |
| domain | `dynu_get_details_domain_registration_domain` | Get details of a domain registration domain. | GET /domain/{id} | id(必填) |
| domain | `dynu_get_list_domains_domain_registration_service` | Get a list of domains for domain registration service. | GET /domain |  |
| email | `dynu_add_new_email_account_email_service` | Add a new email account for email service. | POST /email/{id}/account | id(必填), body(必填,dict) |
| email | `dynu_get_details_email_account` | Get details of the email account. | GET /email/{id}/account/{accountId} | id(必填), account_id(必填) |
| email | `dynu_get_details_email_service` | Get details of an email service. | GET /email/{id} | id(必填) |
| email | `dynu_get_list_email_accounts_email_service` | Get a list of email accounts for email service. | GET /email/{id}/account | id(必填) |
| email | `dynu_get_list_email_services` | Get a list of email services. | GET /email |  |
| email | `dynu_remove_email_account_email_service` | Remove an email account from email service. | DELETE /email/{id}/account/{accountId} | id(必填), account_id(必填) |
| email | `dynu_update_existing_email_account_email_service` | Update an existing email account for email service. | POST /email/{id}/account/{accountId} | id(必填), account_id(必填), body(必填,dict) |
| compute | `dynu_get_instance` | Get an instance. | GET /compute/instance/{id} | id(必填) |
| compute | `dynu_get_list_instances` | Get a list of instances. | GET /compute/instance |  |
| compute | `dynu_start_instance` | Start an instance. | GET /compute/instance/{id}/start | id(必填) |
| compute | `dynu_stop_suspend_instance` | Stop (suspend) an instance. | GET /compute/instance/{id}/stop | id(必填) |
| monitor | `dynu_add_new_monitor` | Add a new monitor. | POST /monitor | body(必填,dict) |
| monitor | `dynu_delete_monitor` | Delete a monitor. | DELETE /monitor/{id} | id(必填) |
| monitor | `dynu_get_details_monitor` | Get details of a monitor. | GET /monitor/{id} | id(必填) |
| monitor | `dynu_get_list_monitors` | Get a list of monitors. | GET /monitor |  |
| monitor | `dynu_limits_associated_monitoring` | Limits associated with monitoring. | GET /monitor/limit |  |
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

- **Trimmed from 117 to 30 tools, by explicit user decision**: the platform
  this MCP runs behind aggregates every enabled vendor MCP's tools into a
  single Gemini/Vertex model call, which caps at 512 total function
  declarations — with 50+ vendor MCPs registered, each needs to stay lean.
  Kept: MSPbots' real `GET /dns` endpoint, core DNS record/service CRUD (8),
  core email service/account CRUD (7), basic compute instance
  list/detail/start/stop (4), domain list/detail (2), and Monitor/Ping in
  full (9). Cut entirely: domain registrar administration (glue records,
  nameservers, auto-renewal, lock/unlock/cancel), email's
  blacklist/whitelist/alias/distribution-list/DKIM management, and compute's
  backup/snapshot/VNC/reinstall/password-change operations. Any of these can
  be re-added on request if a real use case needs them.
- **Compute and domain write operations remain higher-stakes** even after
  trimming — `dynu_start_instance`/`dynu_stop_suspend_instance` act on real
  VPS instances. Treat these as **destructive/irreversible** and confirm
  with a human before invoking.
- **`body` parameters are untyped (`dict`)** rather than fully modeled —
  the OpenAPI spec's Models section defines the exact schema per resource
  (e.g. `DNS.dnsRecordA`), but reproducing all of them as typed Python
  parameters was out of scope. Callers should shape the `body` dict per the
  linked spec.
- Only `dynu_get_list_domains_dns_service` (MSPbots' own endpoint) was
  live-verified with real account data. The remaining 29 tools are
  structurally correct (schema validated, MCP-protocol `tools/list`
  confirmed, tool count re-verified after trimming) but not individually
  smoke-tested — several are write/destructive operations that would
  create, modify, or delete real DNS records, email accounts, or VPS
  instances, so they weren't exercised against the live test account.
