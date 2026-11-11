# ai-code-review-lab

I evaluate AI-generated code solutions, find bugs, test edge cases and compare responses.

## Results

| Problem | Language | Winner | Key finding |
| --- | --- | --- | --- |
| Merge Intervals | Python | Response A | The sweep-line solution (B) fails to merge intervals that only touch, e.g. `[1, 4]` and `[4, 5]`, because end events are processed before start events at the same coordinate. |
| Valid Parentheses | JavaScript | Response A | The counting solution (B) accepts crossed brackets such as `"([)]"` and `"{[(])}"` because counting each type ignores the nesting order. |
