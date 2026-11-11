# Study Notes — Merge Intervals

## The task in plain words

You have a list of intervals like `[[1, 3], [2, 6]]`. Some of them overlap.
You must join the overlapping ones into bigger intervals and return the final
list. Overlapping includes just touching: `[1, 2]` and `[2, 3]` share the point
`2`, so they must become `[1, 3]`.

## Response A — the sort-and-merge idea

Sort the intervals so they start in order. Then keep a list of finished
intervals. For each new interval, look at the last one you kept:

- If the new interval starts before or at the end of the last one, they overlap,
  so stretch the last one's end if needed.
- Otherwise, the new interval is separate, so start a new one.

Because everything is sorted by start, one pass is enough. This is why it
passes every test.

## Response B — the sweep-line idea

Imagine a line and mark each interval's start with `+1` and its end with `-1`.
Sort all the marks. Walk along the line counting how many intervals are open
("active"). When the count returns to zero, an interval is complete.

This is a good idea, and it correctly handles unsorted input and containment.

## Where the bug is and why

The bug is in how the marks are sorted.

Each mark is a tuple `(position, delta)`. Python sorts tuples by the first
value, then the second. So at position `4`, the end mark `(4, -1)` comes before
the start mark `(4, 1)` because `-1 < 1`.

That means when one interval ends exactly where the next begins, the code
closes the interval first and opens the next one second. The two never merge.
In the worst case the counter even goes negative, which is why
`[[1, 1], [1, 1]]` returns `[]`.

The rule is simple: at the same point, a start must be handled before an end,
because touching counts as overlapping.

## The fix

Sort with a tie-break so starts win ties:

```python
events.sort(key=lambda event: (event[0], -event[1]))
```

Now `(4, 1)` comes before `(4, -1)`, and all four failing cases pass.

## Key lesson

When you sort events or records, equal keys are not "no problem". The order of
equal keys is a real decision, and getting it wrong creates bugs that only
appear on exact boundary cases. Always ask: what should happen when two things
share the same coordinate?

## Quiz

1. Response A merges when `start <= last_end`. What changes if you use
   `start < last_end` instead? Which input breaks?

2. Why does `[[1, 1], [1, 1]]` return `[]` in Response B, and what does the
   active counter do at each event?

3. Both solutions are O(n log n). Name one concrete reason to still prefer
   Response A over Response B beyond correctness.
