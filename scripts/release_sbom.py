#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "config" / "rldyour-contract.json"


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def created_timestamp() -> str:
    raw_epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if raw_epoch and raw_epoch.isdigit():
        epoch = int(raw_epoch)
    else:
        epoch = 0
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch))


def build_sbom() -> dict[str, Any]:
    contract = load_json(CONTRACT)
    adapter = contract["adapter"]
    name = str(adapter["name"])
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    runtime_package = str(adapter["runtime_package"])
    runtime_version = str(adapter["runtime_version"])
    root_package = f"SPDXRef-Package-{name}"
    runtime_ref = f"SPDXRef-Package-{runtime_package.replace('@', '').replace('/', '-') }"
    return {
        "spdxVersion": "SPDX-2.3",
        "dataLicense": "CC0-1.0",
        "SPDXID": "SPDXRef-DOCUMENT",
        "name": f"{name}-{version}",
        "documentNamespace": f"https://github.com/NDDev-it-com/{name}/releases/download/{version}/sbom.spdx.json",
        "creationInfo": {
            "created": created_timestamp(),
            "creators": ["Organization: NDDev", "Tool: rldyour-release-sbom"],
        },
        "packages": [
            {
                "name": name,
                "SPDXID": root_package,
                "versionInfo": version,
                "downloadLocation": f"https://github.com/NDDev-it-com/{name}",
                "filesAnalyzed": False,
                "licenseConcluded": "AGPL-3.0-or-later",
                "licenseDeclared": "AGPL-3.0-or-later",
                "copyrightText": "NOASSERTION",
                "supplier": "Organization: NDDev",
            },
            {
                "name": runtime_package,
                "SPDXID": runtime_ref,
                "versionInfo": runtime_version,
                "downloadLocation": "NOASSERTION",
                "filesAnalyzed": False,
                "licenseConcluded": "NOASSERTION",
                "licenseDeclared": "NOASSERTION",
                "copyrightText": "NOASSERTION",
                "supplier": "NOASSERTION",
            },
        ],
        "relationships": [
            {
                "spdxElementId": "SPDXRef-DOCUMENT",
                "relationshipType": "DESCRIBES",
                "relatedSpdxElement": root_package,
            },
            {
                "spdxElementId": root_package,
                "relationshipType": "DEPENDS_ON",
                "relatedSpdxElement": runtime_ref,
            },
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate release SPDX SBOM")
    parser.add_argument("--output", type=Path, help="Write SBOM JSON to this path")
    args = parser.parse_args()
    payload = json.dumps(build_sbom(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
