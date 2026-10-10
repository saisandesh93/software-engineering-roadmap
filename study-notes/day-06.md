# Day 6 — Frequency Counter and Two Sum

## Completed

- Implemented a frequency counter using a dictionary.
- Solved LeetCode 1, **Two Sum**, using a hash map.

## Two Sum review

The solution is correct. It stores each number's index after checking whether its
complement was already seen. That avoids using the same value twice and returns
the two indices as soon as it finds a valid pair.

| Question | Correct answer |
| --- | --- |
| Why use a dictionary? | Lookup of a needed complement is *average* O(1), avoiding comparison of every pair. |
| Time complexity | O(n) average time: one pass, with average O(1) dictionary operations. |
| Extra space complexity | O(n) in the worst case for the `seen` dictionary. |
| Brute-force time complexity | O(n²), because it examines pairs with nested loops. |

> Dictionary operations are not guaranteed O(1) in every theoretical case; the standard expected analysis is average O(1).
