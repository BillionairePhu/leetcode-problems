# 3202. Find the Maximum Length of Valid Subsequence II

Tag: `Array`, `Modulo`, `Dynamic Programming`

Link: [Problem 3202. Find the Maximum Length of Valid Subsequence II](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17)

This is a follow-up problem of [Problem 3201 - Find the Maximum Length of Valid Subsequence I](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/?envType=daily-question&envId=2025-07-16)

## Intuition

The valid subsequence should have all consecutive pair of numbers having the same modulo for their sums.

We can divide it into k cases: the pair having the sum modulo k equal to i with i being from 0 to k-1

Then for each case, we can divide it into sub-cases: for the pair having the sum modulo k equal to i, the starting number of the sequence modulo k can be j with j being from 0 to k-1.

We can use dynamic programming to store the longest sequence for each sub-cases

## Complexity

Time complexity: O(n * k)
- n: the number of integers in the original sequence
- k: the input k for modulo

## Related problems

- [Problem 3201 - Find the Maximum Length of Valid Subsequence I](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/?envType=daily-question&envId=2025-07-16)
