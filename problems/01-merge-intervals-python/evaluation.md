# Merge Intervals: Evaluation

## Prompt

See `prompt.md`. Both models received the same prompt: merge overlapping or
touching intervals, accept unsorted input, and return the result sorted by
start.

## Response A summary

`response_a.py` sorts the intervals by start and then walks through them once,
merging each interval into the last kept interval when its start is less than
or equal to that interval's end. This is the standard "sort and merge"
approach.

## Response B summary

`response_b.py` uses a sweep-line approach. It turns each interval into a
start event `(start, +1)` and an end event `(end, -1)`, sorts the events, and
tracks how many intervals are "active". When the active count drops to zero,
the open interval is closed. It is a different algorithm from A.

## Does it run?

Yes. Both files import and run without errors. Command used:

```
python -m pytest -v
```

Result:

```
4 failed, 22 passed in 0.04s
```

- Response A: 13 passed (12 parametrized cases + 1 no-mutation test).
- Response B: 9 passed, 4 failed.

## Bugs found

Response B has one root-cause bug: at the same coordinate, an end event is
processed before a start event. The events are stored as `(position, delta)`
and sorted as plain tuples, so `(4, -1)` sorts before `(4, 1)`. The active
counter therefore drops to zero before the touching interval is counted, and
the two intervals are never merged. It can even push the active count negative.

Response A has no bug found by these tests.

## Failing edge cases

Response B fails exactly these four cases (real output):

| Input | Expected | Response B output |
| --- | --- | --- |
| `[[1, 4], [4, 5]]` | `[[1, 5]]` | `[[1, 4], [4, 5]]` |
| `[[2, 3], [1, 2]]` | `[[1, 3]]` | `[[1, 2], [2, 3]]` |
| `[[1, 2], [2, 3], [3, 4]]` | `[[1, 4]]` | `[[1, 2], [2, 3], [3, 4]]` |
| `[[1, 1], [1, 1]]` | `[[1, 1]]` | `[]` |

All four share the same cause: intervals that touch at a single point.

## Complexity

- Response A: O(n log n) time for the sort, O(n) extra space.
- Response B: O(n log n) time for sorting 2n events, O(n) extra space for the
  event list (about twice the memory of A).

Both are the same complexity class. The difference is correctness, not speed.

## Comparison

Response A is correct, shorter, and easier to read. Response B is a valid idea
but has a subtle tie-breaking bug. Response B also does more work and uses more
memory for no benefit.

## Verdict

Winner: Response A.

## Feedback for the model

The sweep-line idea is sound, but the events must be ordered so that a start at
a position is processed before an end at the same position. A one-line fix is to
sort with a tie-break:

```python
events.sort(key=lambda event: (event[0], -event[1]))
```

With this fix all four failing cases pass. Test touching intervals
(`[1, 4], [4, 5]`), chained touches, and duplicate points such as `[[1, 1],
[1, 1]]`, because that is where this class of bug hides.
