# Study Notes: Two Sum

## The task in plain words

You get a list of numbers and a target. Find the two numbers that add up to the
target and return their positions in the list. There is always exactly one pair,
and you cannot use the same position twice.

## Response A: the hash map idea

Walk through the list once. For each number, ask: what partner do I need to reach
the target? That partner is `target - number`. If you have already seen that
partner, you are done, and you return its saved index together with the current
index. If not, save the current number and its index and move on.

The map remembers each value and where it was. This gives one pass and keeps the
original indices, which is exactly what the answer needs.

## Response B: the two-pointer idea

Sort the list first. Then put one pointer at the left end and one at the right
end. Look at the sum of the two values. If the sum is too small, move the left
pointer right to get a bigger value. If the sum is too big, move the right
pointer left to get a smaller value. When the sum matches, you found the pair.

This is a good way to find the pair of values, and it uses constant extra space.

## Where the bugs are and why

There are two bugs, and both come from sorting.

First bug: the function returns `left` and `right`, which are positions in the
sorted list. The question asks for positions in the original list. After sorting,
a value has moved, so the position no longer matches where the value started.
For `[3, 2, 4]` the pair is `2` and `4`. In the sorted list `[2, 3, 4]` they sit
at positions 0 and 2, so the code returns `(0, 2)`. In the original list they sit
at positions 1 and 2, so the right answer is `(1, 2)`.

Second bug: `std::sort(nums.begin(), nums.end())` sorts the caller's array in
place. The function signature takes a reference, so the caller's data is
reordered as a side effect. That is surprising and can break other code that
still needs the original order.

Notice that on already-sorted input both bugs stay hidden, because the sorted
positions happen to equal the original positions.

## The fix

Do not sort the input. If you want the two-pointer method, build a vector of
pairs `(value, original_index)`, sort that copy, and return the saved original
indices:

```cpp
std::vector<std::pair<int, int>> pairs;
for (int i = 0; i < (int)nums.size(); ++i) {
    pairs.push_back({nums[i], i});
}
std::sort(pairs.begin(), pairs.end());
```

Then `pairs[left].second` and `pairs[right].second` are the original indices.

## Key lesson

When a problem asks for positions in the original input, sorting the input is
dangerous. Sort a copy that carries the original index, and never change data the
caller still owns. Test with unsorted input, because sorted input hides this kind
of bug.

## Quiz

1. For `[3, 2, 4]` with target 6, why does Response B return `(0, 2)` instead of
   `(1, 2)`?

2. Why does Response B pass the test with `[2, 7, 11, 15]` but fail the test with
   `[3, 2, 4]`?

3. Response A uses O(n) extra space and Response B uses O(1). Given the bugs in
   Response B, explain why the extra space in Response A is worth it here.
