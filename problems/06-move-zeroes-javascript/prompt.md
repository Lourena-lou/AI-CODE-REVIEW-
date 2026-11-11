# Move Zeroes

## Problem

Given an integer array `nums`, move all the `0` values to the end of the array
while keeping the relative order of the non-zero values the same.

Do this in place. Do not return a new array.

## Examples

Input:  `[0, 1, 0, 3, 12]`
Output: `[1, 3, 12, 0, 0]`

Input:  `[0]`
Output: `[0]`

Input:  `[1, 0, 2, 0, 3]`
Output: `[1, 2, 3, 0, 0]`

## Constraints

- `1 <= nums.length <= 10**4`
- `-2**31 <= nums[i] <= 2**31 - 1`
