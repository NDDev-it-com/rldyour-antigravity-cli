import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import gemini_contract


def test_browser_routing_validates():
    gemini_contract.validate_browser_routing()


def test_native_boundaries_validate():
    gemini_contract.validate_native_boundaries()


@pytest.mark.parametrize(
    "stale_transport",
    [
        "| `chrome-devtools` | stdio (`bunx`) | Live debugging |",
        "bunx chrome-devtools-mcp@1.5.0",
        "npx --yes chrome-devtools-mcp@latest",
        '{"command": "bunx", "args": ["chrome-devtools-mcp@1.5.0"]}',
    ],
)
def test_direct_chrome_package_transports_are_rejected(stale_transport):
    with pytest.raises(gemini_contract.ValidationError):
        gemini_contract.validate_browser_transport_text("fixture", stale_transport)


def test_readme_chrome_transport_names_the_managed_wrapper():
    readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8")
    chrome_row = next(line for line in readme.splitlines() if line.startswith("| `chrome-devtools` |"))

    assert "~/.local/bin/chrome-devtools-mcp" in chrome_row
    assert "bunx" not in chrome_row.lower()
