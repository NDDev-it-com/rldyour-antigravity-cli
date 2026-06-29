#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "rldyour-antigravity-cli"


class Failure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(data, dict), f"{path} must contain a JSON object")
    return data


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def checksum_entries(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.split()
        require(len(parts) >= 2, f"invalid checksum line in {path}: {line!r}")
        entries[Path(parts[-1]).name] = parts[0]
    return entries


def validate_spdx(path: Path) -> None:
    payload = load_json(path)
    require(payload.get("spdxVersion") == "SPDX-2.3", "SBOM must use SPDX-2.3")
    require(payload.get("SPDXID") == "SPDXRef-DOCUMENT", "SBOM must define document SPDXID")
    creation = payload.get("creationInfo")
    require(isinstance(creation, dict) and isinstance(creation.get("created"), str), "SBOM must define creationInfo.created")
    packages = payload.get("packages")
    require(isinstance(packages, list) and packages, "SBOM must define non-empty packages")
    relationships = payload.get("relationships")
    require(isinstance(relationships, list) and relationships, "SBOM must define non-empty relationships")
    package_names = {str(item.get("name")) for item in packages if isinstance(item, dict)}
    require(PACKAGE_NAME in package_names, f"SBOM packages must include {PACKAGE_NAME}")
    for package in packages:
        require(isinstance(package, dict), "SBOM package entries must be objects")
        for key in ("name", "SPDXID", "downloadLocation", "filesAnalyzed", "licenseConcluded", "licenseDeclared"):
            require(key in package, f"SBOM package {package.get('name', '<unknown>')} missing {key}")


def validate(dist: Path) -> list[str]:
    archive = dist / f"{PACKAGE_NAME}-source.zip"
    sbom = dist / "sbom.spdx.json"
    checksums = dist / "SHA256SUMS"
    require(archive.is_file(), f"missing release archive: {archive}")
    require(sbom.is_file(), f"missing SBOM: {sbom}")
    require(checksums.is_file(), f"missing SHA256SUMS: {checksums}")
    validate_spdx(sbom)
    entries = checksum_entries(checksums)
    for artifact in (archive, sbom):
        expected = entries.get(artifact.name)
        require(expected is not None, f"SHA256SUMS must include {artifact.name}")
        actual = sha256(artifact)
        require(expected == actual, f"SHA256SUMS mismatch for {artifact.name}")
    return ["ok: release archive, SPDX SBOM, and checksums validated"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated release assets")
    parser.add_argument("dist", type=Path, nargs="?", default=ROOT / "dist")
    args = parser.parse_args()
    try:
        messages = validate(args.dist)
    except (Failure, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("\n".join(messages))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
