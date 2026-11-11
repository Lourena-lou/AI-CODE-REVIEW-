# Study Notes: Longest Substring Without Repeating Characters

## The task in plain words

You get a string. You must find the longest run of characters with no repeats,
where the characters must be next to each other. Return its length.

## Response A: the sliding window with last positions

Keep a window that always has no repeated characters. The window has a left edge
and a right edge. Move the right edge forward one character at a time.

For each new character, check when you last saw it. If you have never seen it, or
you saw it before the left edge, the window is still clean. If you saw it inside
the window, the window is broken, so move the left edge to just after that old
position. This drops only the duplicate and keeps the rest.

A dictionary stores the last index of each character, so each step is fast. The
whole string is scanned once, which gives O(n) time.

## Response B: the sliding window with a set

This version also keeps a window, but stores the characters in a set. When the
new character is already in the set, it clears the whole set and moves the left
edge to the current position.

This looks tidy, and it works on many inputs.

## Where the bug is and why

The bug is the `window.clear()` call. Clearing removes every character, but only
one character actually caused the repeat. The other characters were still fine
and could have been part of the answer.

Take `"dvdf"`. The correct window is `"vdf"`, length 3.

- The window holds `d`, then `d` and `v`.
- The second `d` repeats. The correct move is to drop the first `d` and keep
  `v`, giving `v`, `d`, then `vdf`.
- Response B clears everything instead, so the window becomes just `d`, then
  `df`. It returns 2.

Take `"abcdeaf"`. The correct window is `"bcdeaf"`, length 6. At the second `a`,
the first `a` should leave and `bcde` should stay. Response B clears and loses
`bcde`, so it returns 5.

The bug hides on inputs like `"abcabcbb"` and `"pwwkew"` because there the repeat
happens at the left edge, where clearing and trimming do the same thing.

## The fix

Trim instead of clearing. Move the left edge forward until the repeated character
has left the window:

```python
while s[right] in window:
    window.remove(s[left])
    left += 1
```

Or store the last index of each character, as Response A does, and jump the left
edge to one past the previous occurrence.

## Key lesson

When a window breaks, fix it by the smallest amount that makes it valid again.
Throwing away the whole window loses good data and produces a wrong answer that
only shows up when the repeat is not at the edge.

## Quiz

1. For `"dvdf"`, what should the window look like after the second `d`, and why
   does Response B get length 2 instead of 3?

2. Why does Response B still return the correct answer for `"abcabcbb"`?

3. In Response A, why is the check `last_seen[ch] >= left` important? What goes
   wrong if you drop the `>= left` part?
