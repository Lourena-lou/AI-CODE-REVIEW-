import shutil
import subprocess
from pathlib import Path

import pytest

HERE = Path(__file__).parent
CXX = shutil.which("clang++") or shutil.which("g++")

CASES = [
    ([2, 7, 11, 15], 9, (0, 1)),
    ([3, 2, 4], 6, (1, 2)),
    ([3, 3], 6, (0, 1)),
    ([-1, -2, -3, -4, -5], -8, (2, 4)),
    ([0, 4, 3, 0], 0, (0, 3)),
    ([1, 2, 3, 4, 5], 9, (3, 4)),
    ([-3, 4, 3, 90], 0, (0, 2)),
    ([5, 75, 25], 100, (1, 2)),
    ([2, 5, 5, 11], 10, (1, 2)),
    ([0, 1, 2, 0], 0, (0, 3)),
    ([1, 3, 4, 2], 6, (2, 3)),
]

pytestmark = pytest.mark.skipif(
    CXX is None, reason="a C++ compiler is required to build the solutions"
)


@pytest.fixture(scope="session")
def binaries(tmp_path_factory):
    output = tmp_path_factory.mktemp("two-sum-bin")
    built = {}
    for name in ("response_a", "response_b"):
        binary = output / name
        subprocess.run(
            [
                CXX,
                "-std=c++17",
                "-O2",
                str(HERE / "driver.cpp"),
                str(HERE / f"{name}.cpp"),
                "-o",
                str(binary),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        built[name] = binary
    return built


def evaluate(binary, cases):
    lines = [str(len(cases))]
    for nums, target, _ in cases:
        lines.append(f"{len(nums)} {target}")
        lines.append(" ".join(str(value) for value in nums))
    completed = subprocess.run(
        [str(binary)], input="\n".join(lines) + "\n", capture_output=True, text=True
    )
    assert completed.returncode == 0, completed.stderr
    parsed = []
    for line in completed.stdout.strip().splitlines():
        tokens = line.split()
        if tokens[0] == "none":
            parsed.append((None, int(tokens[2])))
        else:
            parsed.append(((int(tokens[0]), int(tokens[1])), int(tokens[2])))
    return parsed


@pytest.fixture(scope="session")
def results(binaries):
    return {name: evaluate(binary, CASES) for name, binary in binaries.items()}


@pytest.mark.parametrize("index", range(len(CASES)))
def test_response_a_correct(results, index):
    nums, target, expected = CASES[index]
    result, _ = results["response_a"][index]
    assert result == expected, f"nums={nums}, target={target}: expected {expected}, got {result}"


@pytest.mark.parametrize("index", range(len(CASES)))
def test_response_b_correct(results, index):
    nums, target, expected = CASES[index]
    result, _ = results["response_b"][index]
    assert result == expected, f"nums={nums}, target={target}: expected {expected}, got {result}"


@pytest.mark.parametrize("index", range(len(CASES)))
def test_response_a_preserves_input(results, index):
    nums, _, _ = CASES[index]
    _, mutated = results["response_a"][index]
    assert mutated == 0, f"nums={nums} was modified"


@pytest.mark.parametrize("index", range(len(CASES)))
def test_response_b_preserves_input(results, index):
    nums, _, _ = CASES[index]
    _, mutated = results["response_b"][index]
    assert mutated == 0, f"nums={nums} was modified"
