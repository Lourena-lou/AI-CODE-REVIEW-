import importlib.util
from pathlib import Path

import pytest

HERE = Path(__file__).parent


def load_merge(filename):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.merge_intervals


merge_a = load_merge("response_a.py")
merge_b = load_merge("response_b.py")

CASES = [
    ([], []),
    ([[1, 3]], [[1, 3]]),
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [0, 4]], [[0, 4]]),
    ([[1, 4], [2, 3]], [[1, 4]]),
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ([[2, 3], [1, 2]], [[1, 3]]),
    ([[1, 2], [2, 3], [3, 4]], [[1, 4]]),
    ([[-5, -1], [-3, 2]], [[-5, 2]]),
    ([[1, 1], [1, 1]], [[1, 1]]),
    ([[5, 6], [1, 2], [3, 4]], [[1, 2], [3, 4], [5, 6]]),
]


@pytest.mark.parametrize("intervals, expected", CASES)
def test_response_a(intervals, expected):
    assert merge_a(intervals) == expected


@pytest.mark.parametrize("intervals, expected", CASES)
def test_response_b(intervals, expected):
    assert merge_b(intervals) == expected


def test_response_a_does_not_mutate_input():
    intervals = [[1, 4], [0, 4]]
    original = [row[:] for row in intervals]
    merge_a(intervals)
    assert intervals == original


def test_response_b_does_not_mutate_input():
    intervals = [[1, 4], [0, 4]]
    original = [row[:] for row in intervals]
    merge_b(intervals)
    assert intervals == original
