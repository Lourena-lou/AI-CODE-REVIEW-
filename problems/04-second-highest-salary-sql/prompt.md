# Second Highest Salary

## Problem

Table: Employee

| Column | Type |
| --- | --- |
| id | int |
| salary | int |

`id` is the primary key. Each row holds the salary of one employee.

Write a query to find the second highest distinct salary in the table. If there
is no second highest salary, the query must return null as a single row with a
null value.

Return the result as one column named `SecondHighestSalary`.

## Examples

Employee table:

| id | salary |
| --- | --- |
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |

Result: `200`

Employee table:

| id | salary |
| --- | --- |
| 1 | 100 |

Result: `null`

Employee table:

| id | salary |
| --- | --- |
| 1 | 100 |
| 2 | 100 |

Result: `null`
