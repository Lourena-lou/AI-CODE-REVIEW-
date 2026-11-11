import json
import shutil
import subprocess
from pathlib import Path

import pytest

HERE = Path(__file__).parent
NODE = shutil.which("node")

CASES = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([1], [1]),
    ([0, 0, 0], [0, 0, 0]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),
    ([0, 0, 1], [1, 0, 0]),
    ([1, 0], [1, 0]),
    ([0, 1], [1, 0]),
    ([4, 0, 5, 0, 0, 6], [4, 5, 6, 0, 0, 0]),
    ([-1, 0, -2], [-1, -2, 0]),
    ([0, 0, 0, 1], [1, 0, 0, 0]),
    ([2, 1], [2, 1]),
    ([0, 2, 1], [2, 1, 0]),
]

INPUTS = [nums for nums, _ in CASES]

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
    nums, expected = CASES[index]
    actual = results["a"][index]
    assert actual == expected, f"{nums}: expected {expected}, got {actual}"


@pytest.mark.parametrize("index", range(len(CASES)))
def test_response_b(results, index):
    nums, expected = CASES[index]
    actual = results["b"][index]
    assert actual == expected, f"{nums}: expected {expected}, got {actual}"
