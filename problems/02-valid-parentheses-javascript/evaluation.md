# Valid Parentheses: Evaluation

## Prompt

See `prompt.md`. Both models received the same prompt: decide whether a string
of brackets is balanced, with correct types and correct order.

## Response A summary

`response_a.js` uses a stack. It pushes every opening bracket. When it sees a
closing bracket, it pops the stack and checks that the popped bracket is the
matching partner. At the end the stack must be empty. This is the standard
solution.

## Response B summary

`response_b.js` counts each bracket type separately. It keeps a counter for
round, square and curly brackets, increases it on an opening bracket and
decreases it on a closing bracket, and returns false if any counter goes below
zero. It returns true when all three counters end at zero. This is a different
approach from A.

## Does it run?

Yes. Both files load and run without errors. The tests call Node from pytest
through `run_cases.js`. Commands used:

```
node --version
python -m pytest problems/02-valid-parentheses-javascript -q
```

Result:

```
3 failed, 37 passed in 0.24s
```

- Response A: 20 passed.
- Response B: 17 passed, 3 failed.

## Bugs found

Response B has one root-cause bug: counting brackets ignores their order. The
counters only check that the numbers match and never go negative. They do not
check that brackets close in the correct nesting order, so crossed brackets pass.

Response A has no bug found by these tests.

## Failing edge cases

Response B fails exactly these three cases (real output):

| Input | Expected | Response B output |
| --- | --- | --- |
| `"([)]"` | `false` | `true` |
| `"[(])"` | `false` | `true` |
| `"{[(])}"` | `false` | `true` |

All three have the same shape: an opening bracket is closed by the wrong type
before its own partner arrives. The counters balance, so B accepts them.

## Complexity

- Response A: O(n) time, O(n) space for the stack.
- Response B: O(n) time, O(1) space for the counters.

Response B uses less memory, but the memory saving is not worth the wrong
answers.

## Comparison

Response A is correct and still simple. Response B is shorter and uses constant
space, but it solves a different problem: it checks that the counts match, not
that the brackets are properly nested.

## Verdict

Winner: Response A.

## Feedback for the model

A bracket string is valid only when the most recent unclosed bracket is the one
that gets closed next. Counting cannot see that relationship, so the model must
track order. A stack is the direct way to do it. Test crossed input such as
`"([)]"`, `"[(])"` and `"{[(])}"`, because these are the cases that separate
counting from real nesting.
