"""tools/list snapshot + error-envelope mapping tests.

No network calls: tool enumeration goes through FastMCP's in-process
list_tools(), and the error-code mapping is tested directly against
DynuError, independent of any real HTTP request.
"""

import pytest

from dynu_mcp.api_client import DynuError
from dynu_mcp.config import Settings
from dynu_mcp.server import create_mcp_server

# name -> set of required parameter names
EXPECTED_TOOLS = {
    # compute
    "dynu_get_instance": {"id"},
    "dynu_get_list_instances": set(),
    "dynu_start_instance": {"id"},
    "dynu_stop_suspend_instance": {"id"},
    # dns
    "dynu_add_new_dns_record_dns_service": {"id", "body"},
    "dynu_add_new_dns_service": {"body"},
    "dynu_get_details_dns_record_dns_service": {"id", "dns_record_id"},
    "dynu_get_details_domain_dns_service": {"id"},
    "dynu_get_list_dns_records_dns_service": {"id"},
    "dynu_get_list_domains_dns_service": set(),
    "dynu_remove_dns_record_dns_service": {"id", "dns_record_id"},
    "dynu_update_existing_dns_record_dns_service": {"id", "dns_record_id", "body"},
    # domain
    "dynu_get_details_domain_registration_domain": {"id"},
    "dynu_get_list_domains_domain_registration_service": set(),
    # email
    "dynu_add_new_email_account_email_service": {"id", "body"},
    "dynu_get_details_email_account": {"id", "account_id"},
    "dynu_get_details_email_service": {"id"},
    "dynu_get_list_email_accounts_email_service": {"id"},
    "dynu_get_list_email_services": set(),
    "dynu_remove_email_account_email_service": {"id", "account_id"},
    "dynu_update_existing_email_account_email_service": {"id", "account_id", "body"},
    # monitor
    "dynu_add_new_monitor": {"body"},
    "dynu_delete_monitor": {"id"},
    "dynu_get_details_monitor": {"id"},
    "dynu_get_list_monitors": set(),
    "dynu_limits_associated_monitoring": set(),
    "dynu_pause_monitor": {"id"},
    "dynu_unpause_monitor": {"id"},
    # ping
    "dynu_ping_api_server_obtain_pong_response_get": {"message"},
    "dynu_ping_api_server_obtain_pong_response_post": {"body"},
}

# name -> dict of annotation-field -> expected value (only fields we explicitly set)
EXPECTED_ANNOTATIONS = {
    "dynu_get_instance": {"readOnlyHint": True},
    "dynu_get_list_instances": {"readOnlyHint": True},
    "dynu_start_instance": {"destructiveHint": True, "idempotentHint": True},
    "dynu_stop_suspend_instance": {"destructiveHint": True, "idempotentHint": True},
    "dynu_add_new_dns_record_dns_service": {"idempotentHint": False},
    "dynu_add_new_dns_service": {"idempotentHint": False},
    "dynu_get_details_dns_record_dns_service": {"readOnlyHint": True},
    "dynu_get_details_domain_dns_service": {"readOnlyHint": True},
    "dynu_get_list_dns_records_dns_service": {"readOnlyHint": True},
    "dynu_get_list_domains_dns_service": {"readOnlyHint": True},
    "dynu_remove_dns_record_dns_service": {"destructiveHint": True, "idempotentHint": True},
    "dynu_update_existing_dns_record_dns_service": {"idempotentHint": True},
    "dynu_get_details_domain_registration_domain": {"readOnlyHint": True},
    "dynu_get_list_domains_domain_registration_service": {"readOnlyHint": True},
    "dynu_add_new_email_account_email_service": {"idempotentHint": False},
    "dynu_get_details_email_account": {"readOnlyHint": True},
    "dynu_get_details_email_service": {"readOnlyHint": True},
    "dynu_get_list_email_accounts_email_service": {"readOnlyHint": True},
    "dynu_get_list_email_services": {"readOnlyHint": True},
    "dynu_remove_email_account_email_service": {"destructiveHint": True, "idempotentHint": True},
    "dynu_update_existing_email_account_email_service": {"idempotentHint": True},
    "dynu_add_new_monitor": {"idempotentHint": False},
    "dynu_delete_monitor": {"destructiveHint": True, "idempotentHint": True},
    "dynu_get_details_monitor": {"readOnlyHint": True},
    "dynu_get_list_monitors": {"readOnlyHint": True},
    "dynu_limits_associated_monitoring": {"readOnlyHint": True},
    "dynu_pause_monitor": {"idempotentHint": True},
    "dynu_unpause_monitor": {"idempotentHint": True},
    "dynu_ping_api_server_obtain_pong_response_get": {"readOnlyHint": True},
    "dynu_ping_api_server_obtain_pong_response_post": {"readOnlyHint": True},
}


@pytest.mark.asyncio
async def test_tools_list_snapshot():
    mcp = create_mcp_server(Settings())
    tools = await mcp.list_tools()
    names = {t.name for t in tools}
    assert names == set(EXPECTED_TOOLS), f"unexpected tool set: {names}"
    assert len(names) <= 30

    by_name = {t.name: t for t in tools}
    for name, expected_required in EXPECTED_TOOLS.items():
        tool = by_name[name]
        required = set(tool.inputSchema.get("required", []))
        assert required == expected_required, f"{name}: required={required}"
        assert len(tool.description or "") <= 500, f"{name}: description too long"
        first_line = (tool.description or "").strip().splitlines()[0]
        assert len(first_line) <= 100, f"{name}: first line too long: {first_line!r}"
        assert "API:" not in (tool.description or ""), f"{name}: leaks implementation detail"

        expected_annotations = EXPECTED_ANNOTATIONS[name]
        assert tool.annotations is not None, f"{name}: missing annotations"
        for field, expected_value in expected_annotations.items():
            actual_value = getattr(tool.annotations, field)
            assert actual_value == expected_value, (
                f"{name}: annotations.{field}={actual_value}, expected {expected_value}"
            )


@pytest.mark.asyncio
async def test_service_instructions_present_and_bounded():
    mcp = create_mcp_server(Settings())
    assert mcp.instructions
    assert len(mcp.instructions) <= 1500


@pytest.mark.parametrize(
    "status_code,expected_code,expected_retryable",
    [
        (0, "upstream_error", True),
        (400, "invalid_argument", False),
        (401, "unauthorized", False),
        (403, "unauthorized", False),
        (404, "not_found", False),
        (422, "invalid_argument", False),
        (429, "rate_limited", True),
        (500, "upstream_error", True),
        (503, "upstream_error", True),
    ],
)
def test_error_envelope_mapping(status_code, expected_code, expected_retryable):
    import json

    err = DynuError(status_code, "boom")
    envelope = json.loads(err.to_envelope())
    assert envelope["error"]["code"] == expected_code
    assert envelope["error"]["retryable"] is expected_retryable
    assert envelope["error"]["message"] == "boom"
