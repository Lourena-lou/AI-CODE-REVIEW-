# Two Sum: Evaluation

## Prompt

See `prompt.md`. Both models received the same prompt: return the indices of the
two numbers that add up to `target`, with exactly one solution and no reuse of
the same element.

## Response A summary

`response_a.cpp` uses a hash map. It walks the array once. For each value it
computes the needed partner `target - value` and checks whether that partner was
already seen. If so, it returns both indices. This is the standard solution.

## Response B summary

`response_b.cpp` sorts the array and uses two pointers, one at each end. If the
sum is too small it moves the left pointer up, if too large it moves the right
pointer down. When the sum matches, it returns the two pointers. This is a
different approach from A.

## Does it run?

Yes. Both files compile with `clang++ -std=c++17` and run without errors. The
tests compile each response together with `driver.cpp` and run the cases through
pytest. Command used:

```
python -m pytest problems/03-two-sum-cpp -q
```

Result:

```
13 failed, 31 passed in 2.67s
```

- Response A: 22 passed (11 correctness, 11 input-preservation).
- Response B: 9 passed, 13 failed (6 correctness, 7 input-preservation).

## Bugs found

Response B has two bugs.

1. It returns positions in the sorted array, not indices in the original array.
   After sorting, a value sits at a new position, so the returned numbers point
   to the wrong elements.

2. It sorts `nums` in place, so it changes the caller's array. The function
   takes `std::vector<int>&` and modifies it, which the caller does not expect.

Response A has no bug found by these tests.

## Failing edge cases

Response B returns the wrong indices on these six cases (real output):

| nums | target | Expected | Response B output |
| --- | --- | --- | --- |
| `[3, 2, 4]` | 6 | `(1, 2)` | `(0, 2)` |
| `[-1, -2, -3, -4, -5]` | -8 | `(2, 4)` | `(0, 2)` |
| `[0, 4, 3, 0]` | 0 | `(0, 3)` | `(0, 1)` |
| `[-3, 4, 3, 90]` | 0 | `(0, 2)` | `(0, 1)` |
| `[0, 1, 2, 0]` | 0 | `(0, 3)` | `(0, 1)` |
| `[1, 3, 4, 2]` | 6 | `(2, 3)` | `(1, 3)` |

Response B also modified the input on 7 of the 11 cases. It passed the cases
where the input was already sorted, which hides the problem when the tests are
weak.

## Complexity

- Response A: O(n) time, O(n) space for the hash map.
- Response B: O(n log n) time for the sort, O(1) extra space, but it destroys
  the input order.

Response A is faster and does not touch the caller's data.

## Comparison

Response A is correct and keeps the original indices naturally. Response B is a
valid idea, but it must remember the original index of each value and must not
reorder the caller's array. It did neither, so it returns the wrong answer and
has a side effect.

## Verdict

Winner: Response A.

## Feedback for the model

When an algorithm needs sorted data but must return original positions, sort a
copy of `(value, original_index)` pairs, never the input itself. Return the
stored original indices, not the sorted positions. Test with unsorted input and
with repeated values such as `[0, 4, 3, 0]`, because those are the cases that
expose both bugs.
