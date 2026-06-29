from __future__ import annotations

import hashlib
import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import release_sbom
import validate_release_assets


def write_artifacts(dist: Path) -> None:
    dist.mkdir(parents=True)
    archive = dist / "rldyour-antigravity-cli-source.zip"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.writestr("rldyour-antigravity-cli/README.md", "release fixture\n")
    sbom = dist / "sbom.spdx.json"
    sbom.write_text(json.dumps(release_sbom.build_sbom()), encoding="utf-8")
    lines = []
    for path in (archive, sbom):
        lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}")
    (dist / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_release_sbom_has_spdx_shape() -> None:
    payload = release_sbom.build_sbom()
    assert payload["spdxVersion"] == "SPDX-2.3"
    assert payload["SPDXID"] == "SPDXRef-DOCUMENT"
    assert payload["packages"]
    assert payload["relationships"]
    assert any(package["name"] == "rldyour-antigravity-cli" for package in payload["packages"])


def test_release_assets_validate(tmp_path: Path) -> None:
    dist = tmp_path / "dist"
    write_artifacts(dist)

    assert validate_release_assets.validate(dist) == ["ok: release archive, SPDX SBOM, and checksums validated"]


def test_release_assets_reject_marker_sbom(tmp_path: Path) -> None:
    dist = tmp_path / "dist"
    write_artifacts(dist)
    (dist / "sbom.spdx.json").write_text('{"sbom":"source-only"}\n', encoding="utf-8")

    try:
        validate_release_assets.validate(dist)
    except validate_release_assets.Failure as exc:
        assert "SPDX-2.3" in str(exc)
    else:
        raise AssertionError("marker-only SBOM was accepted")
