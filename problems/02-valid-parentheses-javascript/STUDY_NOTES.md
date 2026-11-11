# Study Notes: Valid Parentheses

## The task in plain words

You get a string of brackets like `"([{}])"` or `"([)]"`. You must decide if
every opening bracket is closed by its matching type, in the right order. An
empty string counts as valid.

## Response A: the stack idea

A stack works like a pile of plates. When you see an opening bracket, put it on
top of the pile. When you see a closing bracket, take the top plate off and
check it is the correct partner.

Why this works: the bracket you must close next is always the most recent one
you opened. That is exactly what a stack gives you, last in, first out.

If the pile is empty at the end, everything was closed. If a closing bracket
arrives when the pile is empty, or the top plate does not match, the string is
invalid.

## Response B: the counting idea

Response B counts each bracket type on its own. Three counters go up on opening
brackets and down on closing brackets. If a counter ever goes negative, it
returns false. If all counters end at zero, it returns true.

This catches some mistakes. `")("` fails because the round counter goes
negative right away. `"(]"` fails because the square counter goes negative.

## Where the bug is and why

The bug is that counting throws away order. The counters only know how many of
each bracket type exist, not where they are.

Take `"([)]"`. The round counter goes 1 then 0, and the square counter goes 1
then 0. Everything balances and nothing goes negative, so Response B returns
`true`. But the `(` is closed by `)` only after `[` was opened and closed by
`]`. The nesting is crossed, so the real answer is `false`.

The same thing happens with `"[(])"` and `"{[(])}"`. In each case the totals
match, so the counters are happy, but the order is wrong.

## The fix

Track order, not totals. The cleanest fix is the stack from Response A. If you
had to keep it different, you could remember the last unclosed opening bracket
and compare it, but that is just a stack with one item. The stack is the right
tool.

## Key lesson

Counting tells you how many. It does not tell you the order. Whenever a problem
depends on nesting, pairing or "most recent", reach for a stack instead of a
counter, and always test crossed input like `"([)]"`.

## Quiz

1. Why does `"([)]"` pass Response B even though it is invalid?

2. Response A pops the stack on a closing bracket. What does `stack.pop()`
   return when the stack is empty, and why does that make `")"` fail?

3. Give one input where Response B is correct and Response A is also correct,
   and explain what makes that input easy for both.
