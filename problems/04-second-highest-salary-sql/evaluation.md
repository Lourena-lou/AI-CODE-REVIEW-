# Second Highest Salary: Evaluation

## Prompt

See `prompt.md`. Both models received the same prompt: return the second highest
distinct salary, or a single null row when it does not exist.

## Response A summary

`response_a.sql` finds the highest salary with a subquery, then selects the
maximum salary that is strictly below it. The outer `MAX` always returns exactly
one row. When no salary is below the highest, that row is null, which is what the
problem asks for.

## Response B summary

`response_b.sql` removes duplicates with `DISTINCT`, sorts the salaries from high
to low, and skips the first one with `LIMIT 1 OFFSET 1`. This is a different
approach from A and it is easy to read.

## Does it run?

Yes. Both queries run on SQLite without errors. The tests build an in-memory
database for each case and run the query. Command used:

```
python -m pytest problems/04-second-highest-salary-sql -q
```

Result:

```
3 failed, 17 passed in 0.02s
```

- Response A: 10 passed.
- Response B: 7 passed, 3 failed.

## Bugs found

Response B has one bug: when there is no second highest salary, it returns no
rows instead of a single null row.

The cause is `OFFSET 1`. If the table has fewer than two distinct salaries,
there is no row at offset 1, so the result set is empty. The problem requires one
row that contains null, so an empty result is the wrong shape.

Response A has no bug found by these tests.

## Failing edge cases

Response B fails exactly these three cases (real output):

| Employee salaries | Expected | Response B output |
| --- | --- | --- |
| `[100]` | `[(None,)]` | `[]` |
| `[100, 100]` | `[(None,)]` | `[]` |
| `[]` (empty table) | `[(None,)]` | `[]` |

All three have fewer than two distinct salaries. Note that `[100, 100]` is the
duplicate case: `DISTINCT` leaves one salary, so the second offset is still
missing.

## Complexity

- Response A: two scans of the table, O(n) time, O(1) extra space.
- Response B: O(n log n) time for the sort, O(n) extra space for the distinct
  values.

Both are acceptable for this problem. The difference is the null case, not speed.

## Comparison

Response A is correct in every case and needs no extra work to produce the null
row. Response B is shorter and reads well, but it answers a slightly different
question: "what is the salary at the second position" instead of "what is the
second highest salary, or null".

## Verdict

Winner: Response A.

## Feedback for the model

`ORDER BY ... LIMIT 1 OFFSET 1` returns nothing when the offset is out of range,
so it cannot satisfy a "return null" requirement on its own. To keep that style,
wrap it as a scalar subquery so an empty result becomes null:

```sql
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```

Test with a single distinct salary, with all salaries equal, and with an empty
table, because those are the cases that separate an empty result from a null
value.
