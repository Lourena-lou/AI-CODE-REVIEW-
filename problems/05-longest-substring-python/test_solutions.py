import importlib.util
from pathlib import Path

import pytest

HERE = Path(__file__).parent


def load_solution(filename):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.length_of_longest_substring


length_a = load_solution("response_a.py")
length_b = load_solution("response_b.py")

CASES = [
    ("", 0),
    ("a", 1),
    ("aa", 1),
    ("ab", 2),
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("dvdf", 3),
    ("abba", 2),
    ("tmmzuxt", 5),
    ("aab", 2),
    ("abcdefg", 7),
    (" ", 1),
    ("cdd", 2),
    ("abcb", 3),
    ("abcdeaf", 6),
    ("aabbaa", 2),
    ("12321", 3),
    ("abcdefghijklmnopqrstuvwxyz", 26),
]


@pytest.mark.parametrize("text, expected", CASES)
def test_response_a(text, expected):
    assert length_a(text) == expected


@pytest.mark.parametrize("text, expected", CASES)
def test_response_b(text, expected):
    assert length_b(text) == expected
