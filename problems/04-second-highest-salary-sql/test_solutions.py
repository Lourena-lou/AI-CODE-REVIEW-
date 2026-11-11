import sqlite3
from pathlib import Path

import pytest

HERE = Path(__file__).parent

SCHEMA = "CREATE TABLE Employee (id INTEGER PRIMARY KEY, salary INTEGER)"

CASES = [
    ([100, 200, 300], [(200,)]),
    ([100], [(None,)]),
    ([100, 100], [(None,)]),
    ([100, 200, 200], [(100,)]),
    ([100, 200, 300, 300], [(200,)]),
    ([], [(None,)]),
    ([200, 100], [(100,)]),
    ([100, 200, 300, 400], [(300,)]),
    ([-100, -200], [(-200,)]),
    ([100, 200, 300, 200, 300], [(200,)]),
]


def load_sql(filename):
    return (HERE / filename).read_text()


def run_query(sql, salaries):
    connection = sqlite3.connect(":memory:")
    connection.execute(SCHEMA)
    for index, salary in enumerate(salaries, start=1):
        connection.execute(
            "INSERT INTO Employee (id, salary) VALUES (?, ?)", (index, salary)
        )
    rows = connection.execute(sql).fetchall()
    connection.close()
    return rows


@pytest.mark.parametrize("index", range(len(CASES)))
def test_response_a(index):
    salaries, expected = CASES[index]
    actual = run_query(load_sql("response_a.sql"), salaries)
    assert actual == expected, f"salaries={salaries}: expected {expected}, got {actual}"


@pytest.mark.parametrize("index", range(len(CASES)))
def test_response_b(index):
    salaries, expected = CASES[index]
    actual = run_query(load_sql("response_b.sql"), salaries)
    assert actual == expected, f"salaries={salaries}: expected {expected}, got {actual}"
