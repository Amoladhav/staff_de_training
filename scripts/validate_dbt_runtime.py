"""Verify the local orders workflow in a disposable copy, retaining evidence.

Run with the project Python. Only sanitized project inputs are copied; the
developer's database, profiles and existing artifacts are never used or modified.
"""

from collections import Counter
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    workspace = Path(tempfile.mkdtemp(prefix="staff_de_dbt_v2_"))
    print(f"Evidence directory: {workspace}", flush=True)
    project = workspace / "training_analytics"
    project.mkdir()
    for name in ("dbt_project.yml", "profiles.example.yml", "load_orders.py"):
        shutil.copy2(root / "training_analytics" / name, project / name)
    for name in ("models", "tests", "seeds"):
        shutil.copytree(root / "training_analytics" / name, project / name)
    profiles = workspace / "profiles"
    profiles.mkdir()
    shutil.copy2(project / "profiles.example.yml", profiles / "profiles.yml")
    env = os.environ.copy()
    env.update(
        DBT_PROFILES_DIR=str(profiles),
        DBT_DUCKDB_PATH=str(project / "dev.duckdb"),
        DBT_SEND_ANONYMOUS_USAGE_STATS="false",
        DBT_DISABLE_VERSION_CHECK="true",
    )
    dbt = Path(sys.executable).parent / ("dbt.exe" if os.name == "nt" else "dbt")

    def run(label: str, command: list[str], expected_code: int = 0) -> None:
        result = subprocess.run(
            command, cwd=project, env=env, capture_output=True, text=True,
            timeout=120, check=False,
        )
        (workspace / f"{label}.log").write_text(
            result.stdout + result.stderr, encoding="utf-8"
        )
        if result.returncode != expected_code:
            raise RuntimeError(
                f"{label}: exit {result.returncode}, expected {expected_code}; "
                f"see {workspace / (label + '.log')}"
            )
        print(f"{label}: expected exit {result.returncode}", flush=True)

    def invoke(label: str, args: list[str], expected_code: int = 0) -> None:
        run(label, [
            str(dbt), *args, "--project-dir", str(project),
            "--profiles-dir", str(profiles),
            "--target-path", str(workspace / label),
            "--log-path", str(workspace / "logs" / label),
            "--no-manage-state", "--no-version-check", "--no-send-anonymous-usage-stats",
        ], expected_code)

    summary = {}

    def inspect(label: str, expected: dict[str, int]) -> None:
        artifact = workspace / label / "run_results.json"
        results = json.loads(artifact.read_text(encoding="utf-8"))["results"]
        counts = dict(Counter(row["status"] for row in results))
        if counts != expected:
            raise RuntimeError(f"{label}: unexpected statuses {counts}; see {artifact}")
        source_test = next(
            row for row in results
            if row["unique_id"] == "test.training_analytics.assert_orders_fixture_count"
        )
        expected_failures = 1 if label == "failure" else 0
        if source_test.get("failures") != expected_failures:
            raise RuntimeError(f"{label}: unexpected source-test failure count")
        summary[label] = counts

    run("dependencies", [sys.executable, "-m", "pip", "check"])
    run("version", [str(dbt), "--version"])
    run("load", [sys.executable, str(project / "load_orders.py")])
    invoke("debug", ["debug"])
    invoke("freshness", ["source", "freshness"])
    build = ["build", "--select", "source:commerce.orders+"]
    invoke("baseline", build)
    inspect("baseline", {"success": 3, "pass": 5})
    test = project / "tests" / "assert_orders_fixture_count.sql"
    original = test.read_text(encoding="utf-8")
    if original.count("3 as expected_rows") != 1:
        raise RuntimeError("Fixture expectation changed; review the failure injection")
    try:
        test.write_text(original.replace("3 as expected_rows", "4 as expected_rows"), encoding="utf-8")
        invoke("failure", build, expected_code=1)
        inspect("failure", {"fail": 1, "skipped": 7})
    finally:
        test.write_text(original, encoding="utf-8")
    invoke("recovery", build)
    inspect("recovery", {"success": 3, "pass": 5})
    invoke("preview", ["show", "--select", "completed_orders", "--limit", "10"])
    (workspace / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, subprocess.TimeoutExpired) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(1)
