# Longest Substring Without Repeating Characters: Evaluation

## Prompt

See `prompt.md`. Both models received the same prompt: return the length of the
longest substring with no repeated characters.

## Response A summary

`response_a.py` uses a sliding window with a dictionary that stores the last
index of each character. When a character repeats inside the current window, the
left pointer moves to one position past the previous occurrence. Only the
duplicate is dropped; the rest of the window stays.

## Response B summary

`response_b.py` also uses a sliding window, but keeps the characters in a set.
When it meets a character already in the set, it clears the whole set and
restarts the window at the current position. This is a different way to manage
the window.

## Does it run?

Yes. Both files run without errors. Command used:

```
python -m pytest problems/05-longest-substring-python -q
```

Result:

```
2 failed, 36 passed in 0.02s
```

- Response A: 19 passed.
- Response B: 17 passed, 2 failed.

## Bugs found

Response B has one bug: on a repeat it clears the entire window instead of
removing only the characters up to the duplicate. Clearing throws away
characters that are still valid and could extend the answer.

Response A has no bug found by these tests.

## Failing edge cases

Response B fails these two cases (real output):

| Input | Expected | Response B output |
| --- | --- | --- |
| `"dvdf"` | `3` | `2` |
| `"abcdeaf"` | `6` | `5` |

For `"dvdf"` the correct window is `"vdf"`, length 3. When the second `d`
appears, only the first `d` should leave the window, but Response B clears
everything and keeps `"df"`, length 2.

For `"abcdeaf"` the correct window is `"bcdeaf"`, length 6. When the second `a`
appears, only the first `a` should leave, but Response B clears the window and
loses `"bcde"`, so it returns 5.

Both failures share the same cause: clearing removes characters that should have
stayed.

## Complexity

- Response A: O(n) time, O(min(n, alphabet)) space.
- Response B: O(n) time, O(alphabet) space.

Both are O(n) time. The difference is correctness, not speed.

## Comparison

Response A is correct because it moves the left edge only as far as needed.
Response B is simpler to write but its reset is too aggressive. Note that
Response B still passes common inputs such as `"abcabcbb"` and `"pwwkew"`, so the
bug stays hidden unless the test includes a case like `"dvdf"`.

## Verdict

Winner: Response A.

## Feedback for the model

Never clear the whole window on a repeat. Move the left pointer forward one step
at a time until the repeated character has left the window, or jump it to one
past the previous occurrence and remove exactly the characters that leave. Test
with `"dvdf"` and `"abcdeaf"`, because a repeat that is not at the window edge is
what exposes this bug.
