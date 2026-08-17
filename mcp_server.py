#!/usr/bin/env python3
"""
SAP Scope Item MCP Server

Exposes the SAP S/4HANA best-practice scope-item lookup as an MCP tool,
so any MCP-compatible client (Claude Desktop, another agent, the
orchestrator) can query the catalogue without importing this codebase.

Usage:
    # stdio transport (default — used by Claude Desktop and MCP clients)
    python mcp_server.py

    # Test the tool directly (no MCP, prints JSON)
    python mcp_server.py --test "finance"
    python mcp_server.py --test "MM"

Configuration (Claude Desktop / claude_desktop_config.json):
    {
      "mcpServers": {
        "sap-scope-items": {
          "command": "python",
          "args": ["/path/to/ScopingAgent/mcp_server.py"]
        }
      }
    }
"""

import argparse
import json
import sys

# ── Scope Item Catalogue ─────────────────────────────────────

# A curated subset of SAP S/4HANA scope items relevant to common
# mid-market implementations. Each entry maps an SAP scope item ID
# to its module, functional area, and deployment edition.

SCOPE_ITEMS = {
    "1YB": {"name": "General Ledger Accounting", "module": "FI", "area": "Finance", "edition": "Cloud/OP"},
    "2WB": {"name": "Accounts Payable", "module": "FI-AP", "area": "Finance", "edition": "Cloud/OP"},
    "1F7": {"name": "Accounts Receivable", "module": "FI-AR", "area": "Finance", "edition": "Cloud/OP"},
    "4GR": {"name": "Asset Accounting", "module": "FI-AA", "area": "Finance", "edition": "Cloud/OP"},
    "1NZ": {"name": "Bank Account Management", "module": "FI", "area": "Finance", "edition": "Cloud/OP"},
    "J58": {"name": "Cost Center Accounting", "module": "CO", "area": "Controlling", "edition": "Cloud/OP"},
    "1SO": {"name": "Profitability Analysis", "module": "CO-PA", "area": "Controlling", "edition": "Cloud/OP"},
    "BMD": {"name": "Purchase Order Processing", "module": "MM", "area": "Procurement", "edition": "Cloud/OP"},
    "2NM": {"name": "Supplier Evaluation", "module": "MM", "area": "Procurement", "edition": "Cloud/OP"},
    "BD2": {"name": "Sales Order Management", "module": "SD", "area": "Sales", "edition": "Cloud/OP"},
    "BKP": {"name": "Billing and Invoicing", "module": "SD", "area": "Sales", "edition": "Cloud/OP"},
    "1E6": {"name": "Foreign Trade / Export", "module": "GTS", "area": "Trade Compliance", "edition": "OP"},
    "3EN": {"name": "Batch Management", "module": "MM/PP", "area": "Logistics", "edition": "Cloud/OP"},
    "2QH": {"name": "Quality Inspection", "module": "QM", "area": "Quality", "edition": "Cloud/OP"},
    "1YW": {"name": "Warehouse Management", "module": "EWM", "area": "Logistics", "edition": "Cloud/OP"},
    "4DV": {"name": "Production Planning", "module": "PP", "area": "Manufacturing", "edition": "Cloud/OP"},
    "2V4": {"name": "Material Requirements Planning", "module": "PP-MRP", "area": "Manufacturing", "edition": "Cloud/OP"},
    "1O3": {"name": "Plant Maintenance", "module": "PM", "area": "Asset Management", "edition": "Cloud/OP"},
    "BJ0": {"name": "Predictive Maintenance", "module": "PM", "area": "Asset Management", "edition": "Cloud"},
    "3OP": {"name": "Integration with SAP Analytics Cloud", "module": "BTP", "area": "Analytics", "edition": "Cloud"},
}


def search_scope_items(query: str) -> list[dict]:
    """Search scope items by module, area, name, or ID."""
    q = query.lower()
    results = []
    for item_id, item in SCOPE_ITEMS.items():
        if (
            q in item["module"].lower()
            or q in item["area"].lower()
            or q in item["name"].lower()
            or q in item_id.lower()
        ):
            results.append({"id": item_id, **item})
    return results


# ── MCP Server ────────────────────────────────────────────────

def run_mcp_server():
    """Run the MCP server over stdio transport."""
    from mcp.server.mcpserver import MCPServer

    mcp = MCPServer(
        name="sap-scope-items",
        description=(
            "Look up SAP S/4HANA best-practice scope items by module code, "
            "functional area, or keyword. Returns scope item IDs, names, "
            "modules, and deployment editions."
        ),
    )

    @mcp.tool()
    def lookup_scope_items(query: str) -> str:
        """Search SAP S/4HANA scope items by module code (e.g. 'FI', 'MM'),
        functional area (e.g. 'Finance', 'Logistics'), or keyword
        (e.g. 'batch', 'export', 'maintenance').

        Returns matching scope items with their IDs, names, SAP modules,
        and deployment editions (Cloud, On-Premise, or both).
        """
        results = search_scope_items(query)
        if not results:
            return json.dumps({"matches": 0, "message": f"No scope items matched '{query}'."})
        return json.dumps({"matches": len(results), "items": results}, indent=2)

    @mcp.tool()
    def list_all_scope_items() -> str:
        """List every scope item in the catalogue. Use this to see the full
        set of available SAP S/4HANA best-practice scope items."""
        items = [{"id": k, **v} for k, v in SCOPE_ITEMS.items()]
        return json.dumps({"total": len(items), "items": items}, indent=2)

    mcp.run(transport="stdio")


# ── CLI ───────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="SAP Scope Item MCP Server"
    )
    parser.add_argument(
        "--test", type=str, metavar="QUERY",
        help="Test the lookup locally (no MCP, prints JSON and exits)",
    )
    args = parser.parse_args()

    if args.test:
        results = search_scope_items(args.test)
        print(json.dumps({"matches": len(results), "items": results}, indent=2))
        return

    run_mcp_server()


if __name__ == "__main__":
    main()
