import json
import shutil
import subprocess
from pathlib import Path

import pytest

HERE = Path(__file__).parent
NODE = shutil.which("node")

CASES = [
    ("", True),
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("(", False),
    (")", False),
    ("(((((", False),
    (")))))", False),
    ("((", False),
    ("(())", True),
    ("{[()]}", True),
    ("((()))", True),
    ("()[{}]", True),
    ("[(])", False),
    ("{[(])}", False),
    ("()()()", True),
    ("[]{}()", True),
    ("(((((((((())))))))))", True),
]

INPUTS = [source for source, _ in CASES]

pytestmark = pytest.mark.skipif(
    NODE is None, reason="node is required to run the JavaScript solutions"
)


def run(filename, inputs):
    completed = subprocess.run(
        [NODE, str(HERE / "run_cases.js"), str(HERE / filename), json.dumps(inputs)],
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    return json.loads(completed.stdout)


@pytest.fixture(scope="session")
def results():
    return {
        "a": run("response_a.js", INPUTS),
        "b": run("response_b.js", INPUTS),
    }


@pytest.mark.parametrize("index", range(len(CASES)))
def test_response_a(results, index):
    source, expected = CASES[index]
    actual = results["a"][index]
    assert actual == expected, f"{source!r}: expected {expected}, got {actual}"


@pytest.mark.parametrize("index", range(len(CASES)))
def test_response_b(results, index):
    source, expected = CASES[index]
    actual = results["b"][index]
    assert actual == expected, f"{source!r}: expected {expected}, got {actual}"
