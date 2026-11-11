# Study Notes: Second Highest Salary

## The task in plain words

You have a table of employee salaries. You must find the second highest distinct
salary. If there is no second highest salary, you must return a single row that
contains null, not an empty result.

## Response A: the MAX and subquery idea

Find the highest salary first, using `(SELECT MAX(salary) FROM Employee)`. Then
find the highest salary that is strictly smaller than that value:

```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```

An aggregate like `MAX` always returns exactly one row. If no salary passes the
`WHERE` test, the aggregate is computed over zero rows and returns null. That is
why this version produces the null row automatically.

## Response B: the sort and offset idea

Remove duplicates with `DISTINCT`, sort from high to low, then take the row at
offset 1, which is the second one:

```sql
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

This is a normal way to get the second row of a sorted list.

## Where the bug is and why

The bug appears only when the offset points past the end of the data.

`OFFSET 1` means "skip the first row and return the next one". If the sorted
distinct list has only one row, or no rows at all, there is nothing to return, so
the query returns an empty result.

That is different from null. Null is one row whose value is unknown. An empty
result is zero rows. The problem asks for the first one, so the empty result
fails.

The two cases that trigger it are a table with a single distinct salary (for
example `[100]` or `[100, 100]`) and an empty table.

## The fix

You can keep the sorted approach, but wrap it so that an empty result becomes
null:

```sql
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```

A scalar subquery in the `SELECT` list returns null when the inner query finds no
rows, which gives the required single null row.

## Key lesson

"Return null when there is nothing" is not the same as "return no rows". Always
check what your query does at the empty and single-row boundaries, because those
are where `LIMIT` and `OFFSET` quietly change the shape of the result.

## Quiz

1. Why does Response B return an empty result for `[100, 100]`, even though the
   table has two rows?

2. Response A uses `salary < (SELECT MAX(salary) FROM Employee)`. Why does it
   still return one row with null when the table is empty?

3. Suppose the problem asked for the second highest salary but allowed an empty
   result instead of null. Which response would be acceptable then, and why?
