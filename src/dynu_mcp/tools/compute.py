import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import DynuClient, DynuError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], DynuClient | None]) -> None:

    @mcp.tool()
    async def dynu_change_operating_system_password(id: int, body: dict) -> str:
        """Change the operating system password.

        API: POST /compute/instance/{id}/password

        Args:
            id: Required. The id of the instance.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/password"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_change_vnc_password(id: int, body: dict) -> str:
        """Change the VNC password.

        API: POST /compute/instance/{id}/vnc

        Args:
            id: Required. The id of the instance.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/vnc"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_create_manual_backup(id: int) -> str:
        """Create a manual backup.

        API: POST /compute/instance/{id}/backup

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/backup"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_create_or_update_reverse_dns_mapping(id: int, body: dict) -> str:
        """Create or update a reverse DNS mapping.

        API: POST /compute/instance/{id}/reversedns

        Args:
            id: Required. The id of the instance.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/reversedns"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_create_snapshot(id: int) -> str:
        """Create a snapshot.

        API: POST /compute/instance/{id}/snapshot

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/snapshot"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_instance(id: int) -> str:
        """Get an instance.

        API: GET /compute/instance/{id}

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_active_tasks(id: int) -> str:
        """Get a list of active tasks.

        API: GET /compute/instance/{id}/task

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/task"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_backups(id: int) -> str:
        """Get a list of backups.

        API: GET /compute/instance/{id}/backup

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/backup"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_instances() -> str:
        """Get a list of instances.

        API: GET /compute/instance

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/compute/instance", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_operating_systems_available_reinstall() -> str:
        """Get a list of operating systems available for reinstall.

        API: GET /compute/os

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/compute/os", params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_list_snapshots(id: int) -> str:
        """Get a list of snapshots.

        API: GET /compute/instance/{id}/snapshot

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/snapshot"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_network_settings(id: int) -> str:
        """Get network settings.

        API: GET /compute/instance/{id}/network

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/network"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_reverse_dns_mappings(id: int) -> str:
        """Get reverse DNS mappings.

        API: GET /compute/instance/{id}/reversedns

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/reversedns"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_get_vnc_connection_details(id: int) -> str:
        """Get VNC connection details.

        API: GET /compute/instance/{id}/vnc

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/vnc"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_mount_iso_image(id: int, body: dict) -> str:
        """Mount an ISO image.

        API: POST /compute/instance/{id}/mountiso

        Args:
            id: Required. The id of the instance.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/mountiso"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_reinstall_operating_system(id: int, body: dict) -> str:
        """Reinstall the operating system.

        API: POST /compute/instance/{id}/reinstall

        Args:
            id: Required. The id of the instance.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/reinstall"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_all_snapshots(id: int) -> str:
        """Remove all snapshots.

        API: DELETE /compute/instance/{id}/snapshot

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/snapshot"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_backup(id: int, backup_id: int) -> str:
        """Remove a backup.

        API: DELETE /compute/instance/{id}/backup/{backupId}

        Args:
            id: Required. The id of the instance.
            backup_id: Required. The id of the backup.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/backup/{backup_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_ipv6_reverse_dns_mapping(id: int, ptr_record_id: int) -> str:
        """Remove an IPv6 reverse DNS mapping.

        API: DELETE /compute/instance/{id}/reversedns/{ptrRecordId}

        Args:
            id: Required. The id of the instance.
            ptr_record_id: Required. The id of the PTR record.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/reversedns/{ptr_record_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_remove_snapshot(id: int, snapshot_id: int) -> str:
        """Remove a snapshot.

        API: DELETE /compute/instance/{id}/snapshot/{snapshotId}

        Args:
            id: Required. The id of the instance.
            snapshot_id: Required. The id of the snapshot.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/snapshot/{snapshot_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_restart_instance(id: int) -> str:
        """Restart an instance.

        API: GET /compute/instance/{id}/restart

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/restart"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_restore_backup(id: int, backup_id: int) -> str:
        """Restore a backup.

        API: GET /compute/instance/{id}/backup/{backupId}/restore

        Args:
            id: Required. The id of the instance.
            backup_id: Required. The id of the backup.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/backup/{backup_id}/restore"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_restore_snapshot(id: int, snapshot_id: int) -> str:
        """Restore a snapshot.

        API: GET /compute/instance/{id}/snapshot/{snapshotId}/restore

        Args:
            id: Required. The id of the instance.
            snapshot_id: Required. The id of the snapshot.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/snapshot/{snapshot_id}/restore"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_start_instance(id: int) -> str:
        """Start an instance.

        API: GET /compute/instance/{id}/start

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/start"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_stop_suspend_instance(id: int) -> str:
        """Stop (suspend) an instance.

        API: GET /compute/instance/{id}/stop

        Args:
            id: Required. The id of the instance.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/stop"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_unmount_iso_image(id: int, body: dict) -> str:
        """Unmount the ISO image.

        API: POST /compute/instance/{id}/unmountiso

        Args:
            id: Required. The id of the instance.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}/unmountiso"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def dynu_update_instance_label_or_cpu_emulation_mode(id: int, body: dict) -> str:
        """Update an instance label or CPU emulation mode.

        API: POST /compute/instance/{id}

        Args:
            id: Required. The id of the instance.
            body: Required. Request payload (dict) — see the vendor's OpenAPI spec (Models section) for the exact schema of this resource.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/compute/instance/{id}"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except DynuError as e:
            return f"Error: {e}"
