import copy
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import gemini_contract


def test_browser_routing_validates():
    gemini_contract.validate_browser_routing()


@pytest.mark.parametrize("surface", sorted(gemini_contract.BROWSER_EXECUTION_SURFACES))
def test_every_browser_execution_surface_has_exact_boundary(surface):
    text = (Path(__file__).resolve().parents[1] / surface).read_text(encoding="utf-8")
    assert text.count(gemini_contract.MANDATORY_BROWSER_BOUNDARY) == 1


def test_webwright_cannot_become_an_active_provider():
    mutated = copy.deepcopy(gemini_contract.EXPECTED_BROWSER_POLICY)
    mutated["active_providers"].append("webwright")
    with pytest.raises(gemini_contract.ValidationError, match="exactly match"):
        gemini_contract.validate_browser_policy_object(mutated)


def test_missing_browser_boundary_fails_closed():
    with pytest.raises(gemini_contract.ValidationError, match="must appear exactly once"):
        gemini_contract.validate_browser_execution_surface(
            "fixture", "webwright-task never authorizes Webwright runtime execution"
        )


@pytest.mark.parametrize(
    "alternate",
    [
        "/tmp/playwright-cli",
        "/tmp/chrome-devtools-mcp",
        "/tmp/$HOME/.local/bin/playwright-cli",
    ],
)
def test_alternate_browser_provider_path_is_rejected(alternate):
    text = (
        gemini_contract.MANDATORY_BROWSER_BOUNDARY
        + "\n\nwebwright-task never authorizes Webwright runtime execution\n"
        + alternate
    )
    with pytest.raises(gemini_contract.ValidationError, match="must use exact"):
        gemini_contract.validate_browser_execution_surface("fixture", text)


def test_playwright_action_without_immediate_health_gate_is_rejected():
    text = (
        gemini_contract.MANDATORY_BROWSER_BOUNDARY
        + "\n\nwebwright-task never authorizes Webwright runtime execution\n"
        + "```bash\n$HOME/.local/bin/playwright-cli open https://example.test\n```\n"
    )
    with pytest.raises(gemini_contract.ValidationError, match="immediately health-gated"):
        gemini_contract.validate_browser_execution_surface("fixture", text)


@pytest.mark.parametrize(
    "command",
    [
        "npx playwright test",
        "bunx @playwright/test",
        "python3 -m webwright run workflow.py",
        "playwright test",
    ],
)
def test_unapproved_browser_shell_execution_is_rejected(command):
    text = (
        gemini_contract.MANDATORY_BROWSER_BOUNDARY
        + "\n\nwebwright-task never authorizes Webwright runtime execution\n"
        + f"```bash\n{command}\n```\n"
    )
    with pytest.raises(gemini_contract.ValidationError, match="unapproved browser shell"):
        gemini_contract.validate_browser_execution_surface("fixture", text)


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

    assert "$HOME/.local/bin/chrome-devtools-mcp" in chrome_row
    assert "bunx" not in chrome_row.lower()
