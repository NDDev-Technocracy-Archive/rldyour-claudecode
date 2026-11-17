from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github/workflows"
WORKFLOW_DOC = WORKFLOWS / "README.md"
SHARED_REPO = "NDDev-Technocracy-OpenNetwork/nddev-ci"
PIN_RE = re.compile(
    rf"^\s*(?:-\s*)?uses:\s*{re.escape(SHARED_REPO)}/[^@\s]+@"
    r"(?P<sha>[0-9a-f]{40})\s+#\s*(?P<version>v\d+\.\d+\.\d+)\s*$"
)


def test_all_shared_workflow_callers_use_one_declared_release() -> None:
    callers: list[tuple[Path, int, str]] = []
    for path in sorted(WORKFLOWS.glob("*.yml")):
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if "uses:" in line:
                assert "std-0004-ci-cd-workflows/" not in line, path
            if f"{SHARED_REPO}/" in line:
                callers.append((path, line_number, line))

    assert callers, "no shared CI callers found"
    selections: set[tuple[str, str]] = set()
    canonical: tuple[str, str] | None = None
    for path, line_number, line in callers:
        match = PIN_RE.fullmatch(line)
        assert match is not None, f"{path}:{line_number}: invalid shared pin"
        selection = (match["sha"], match["version"])
        selections.add(selection)
        if path.name == "validate.yml" and canonical is None:
            canonical = selection

    # Actual released-source/native qualification belongs to CI and the updater.
    # A second editable SHA in this test cannot establish that provenance.
    assert canonical is not None, "the authoritative validate.yml caller is missing"
    assert selections == {canonical}, "shared workflow pin drift"


def test_shared_workflow_pin_is_documented() -> None:
    text = WORKFLOW_DOC.read_text(encoding="utf-8")
    assert SHARED_REPO in text
    assert "[validate.yml](validate.yml)" in text
