# Merge Intervals

## Problem

Given a list of intervals `intervals`, where each interval is a pair
`[start, end]`, merge every pair of overlapping or touching intervals and
return the list of non-overlapping intervals that covers all of the input.

Two intervals overlap or touch when the start of one is less than or equal to
the end of the other. For example, `[1, 2]` and `[2, 3]` must be merged because
they touch at `2`.

The input is not guaranteed to be sorted. Return the result sorted by start.

## Examples

Input:  `[[1, 3], [2, 6], [8, 10], [15, 18]]`
Output: `[[1, 6], [8, 10], [15, 18]]`

Input:  `[[1, 4], [4, 5]]`
Output: `[[1, 5]]`

Input:  `[[1, 4], [2, 3]]`
Output: `[[1, 4]]`

## Constraints

- `0 <= len(intervals) <= 10**4`
- `start <= end` for every interval
