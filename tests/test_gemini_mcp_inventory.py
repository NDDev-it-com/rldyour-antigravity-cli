import copy
import json
import sys
from pathlib import Path

import pytest

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


def test_refreshed_mcp_runtime_pins_validate():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "gemini-extension.json").read_text(encoding="utf-8"))
    settings = json.loads((root / ".gemini/settings.json").read_text(encoding="utf-8"))
    antigravity = json.loads((root / ".gemini/antigravity-cli/mcp_config.json").read_text(encoding="utf-8"))
    contract = json.loads((root / "config/rldyour-contract.json").read_text(encoding="utf-8"))

    gemini_contract.validate_mcp_runtime_pins(
        {
            "gemini-extension.json": manifest["mcpServers"],
            ".gemini/settings.json": settings["mcpServers"],
            ".gemini/antigravity-cli/mcp_config.json": antigravity["mcpServers"],
        },
        contract,
    )


def test_refreshed_mcp_runtime_pin_drift_is_rejected():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "gemini-extension.json").read_text(encoding="utf-8"))
    settings = copy.deepcopy(manifest)
    antigravity = copy.deepcopy(manifest)
    contract = json.loads((root / "config/rldyour-contract.json").read_text(encoding="utf-8"))
    settings["mcpServers"]["context7"]["args"] = ["@upstash/context7-mcp@3.2.2"]

    with pytest.raises(gemini_contract.ValidationError, match="context7 must pin"):
        gemini_contract.validate_mcp_runtime_pins(
            {
                "gemini-extension.json": manifest["mcpServers"],
                ".gemini/settings.json": settings["mcpServers"],
                ".gemini/antigravity-cli/mcp_config.json": antigravity["mcpServers"],
            },
            contract,
        )
