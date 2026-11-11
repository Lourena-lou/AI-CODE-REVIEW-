# Study Notes: Move Zeroes

## The task in plain words

You have an array of numbers. You must push every zero to the end and keep the
other numbers in the same order they had before. You must change the array itself
and not build a new one.

## Response A: the write index idea

Keep a pointer called `insert`. It marks the next position where a non-zero value
should go. Start it at 0.

Scan the array with a second pointer `i`. Whenever `nums[i]` is not zero, swap it
into position `insert` and move `insert` forward by one.

Because you only ever move non-zero values forward in the order you meet them,
their relative order never changes. The zeros are left behind and end up at the
back. One pass, no extra array.

## Response B: the two-ended swap idea

This version puts one pointer at the start and one at the end. When the left
value is zero, it swaps that zero with the value at the right end and moves the
right pointer left.

The zeros do collect at the back, so it looks like it works.

## Where the bug is and why

The bug is the swap with the end. When you swap a zero with the value at the
right pointer, you drag that value from the end to the front. That value may
belong after other values, so its order breaks.

Take `[0, 1, 0, 3, 12]`. The expected result is `[1, 3, 12, 0, 0]`.

- The left pointer sees `0`, so it swaps with the last value `12`. The array
  becomes `[12, 1, 0, 3, 0]`.
- The `12` has jumped to the front, ahead of `1` and `3`, which is wrong.

The same thing happens in `[1, 0, 2, 0, 3]`, where `3` is pulled in front of `2`.

The bug hides on inputs such as `[0, 1]` and `[0, 0, 1]` because there the swap
happens to leave the order correct.

## The fix

Move values with a stable scan instead of swapping from the end:

```js
let insert = 0;
for (let i = 0; i < nums.length; i++) {
  if (nums[i] !== 0) {
    const temp = nums[insert];
    nums[insert] = nums[i];
    nums[i] = temp;
    insert++;
  }
}
```

This keeps the order and still runs in one pass.

## Key lesson

"Move all zeros to the end" and "keep the order of the rest" are two separate
requirements. A swap from the ends can satisfy the first while breaking the
second. Always test with an input where the values are out of order, not just an
input that checks the zeros moved.

## Quiz

1. For `[0, 2, 1]`, why does Response B return `[1, 2, 0]` instead of `[2, 1, 0]`?

2. Why does Response B give the correct answer for `[0, 0, 1]` but the wrong
   answer for `[0, 2, 1]`?

3. Response A uses a `insert` write index. Explain in one sentence why this keeps
   the non-zero values in order.
