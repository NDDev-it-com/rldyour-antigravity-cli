import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import gemini_contract


def test_mcp_inventory_validates():
    gemini_contract.validate_mcp_inventory()


def test_mcp_surface_equivalence_rejects_url_drift():
    manifest = {
        "mcpServers": {
            alias: {"url": "https://example.test/mcp", "timeout": 1000}
            for alias in gemini_contract.EXPECTED_MCP
        }
    }
    settings = {
        "mcpServers": {
            alias: {"url": "https://example.test/mcp", "timeout": 1000}
            for alias in gemini_contract.EXPECTED_MCP
        }
    }
    antigravity = {
        "mcpServers": {
            alias: {"url": "https://example.test/mcp", "timeout": 1000}
            for alias in gemini_contract.EXPECTED_MCP
        }
    }
    settings["mcpServers"]["figma"] = {"url": "http://127.0.0.1:3845/mcp", "timeout": 1000}

    try:
        gemini_contract.validate_mcp_surface_equivalence(manifest, settings, antigravity)
    except gemini_contract.ValidationError as exc:
        assert "figma" in str(exc)
    else:
        raise AssertionError("MCP URL drift was not rejected")


def test_retired_residue_validates():
    gemini_contract.validate_retired_residue()
