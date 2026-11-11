# Move Zeroes: Evaluation

## Prompt

See `prompt.md`. Both models received the same prompt: move every zero to the
end of the array in place, keeping the relative order of the non-zero values.

## Response A summary

`response_a.js` keeps a write index that marks the next spot for a non-zero
value. It scans the array once. Every non-zero value is swapped into the write
position, and the write index moves forward. This is a stable partition, so the
non-zero values keep their order.

## Response B summary

`response_b.js` uses two pointers, one at the start and one at the end. When the
left value is zero, it swaps it with the value at the right pointer and moves the
right pointer left. This is a different approach from A.

## Does it run?

Yes. Both files run without errors. The tests call Node from pytest. Command
used:

```
python -m pytest problems/06-move-zeroes-javascript -q
```

Result:

```
4 failed, 24 passed in 0.25s
```

- Response A: 14 passed.
- Response B: 10 passed, 4 failed.

## Bugs found

Response B has one bug: it does not keep the relative order of the non-zero
values. Swapping a zero with the last element pulls that last value to the front,
which changes the order.

Response A has no bug found by these tests.

## Failing edge cases

Response B fails these four cases (real output):

| Input | Expected | Response B output |
| --- | --- | --- |
| `[0, 1, 0, 3, 12]` | `[1, 3, 12, 0, 0]` | `[12, 1, 3, 0, 0]` |
| `[1, 0, 2, 0, 3]` | `[1, 2, 3, 0, 0]` | `[1, 3, 2, 0, 0]` |
| `[4, 0, 5, 0, 0, 6]` | `[4, 5, 6, 0, 0, 0]` | `[4, 6, 5, 0, 0, 0]` |
| `[0, 2, 1]` | `[2, 1, 0]` | `[1, 2, 0]` |

In every case the zeros end up at the back, which is why the bug is easy to miss
if you only check that the zeros moved. The order of the remaining values is
wrong.

## Complexity

- Response A: O(n) time, O(1) extra space.
- Response B: O(n) time, O(1) extra space.

Both are O(n) time and use no extra space. The difference is correctness.

## Comparison

Response A is correct because it moves values with a stable scan. Response B is a
valid way to collect zeros at the end, but its swap breaks the order. Response B
passes inputs where the zeros sit at the ends, such as `[0, 1]` and `[0, 0, 1]`,
so weak tests would not catch it.

## Verdict

Winner: Response A.

## Feedback for the model

When a problem says "keep the relative order", you must use a stable move, not an
arbitrary swap. A single write index that copies non-zero values forward and then
fills the tail with zeros does this correctly. Test with `[0, 1, 0, 3, 12]` and
`[0, 2, 1]`, because those show that the values are reordered, not just that the
zeros moved.
