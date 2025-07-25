# 🧠 Leetcode Problem 3487

> A very simple question that asks you to get a subsequence (subarray after deleting some element = subsequence!!!) such that the elements in it is unique and has the maximum sum.

## ✅ Solution Strategy

Divide into 2 cases:
- If the whole given array is full of negative number, return the largest number in it. Because adding any non negative will make the sum smaller.
- Else, return the sum of non-negative numbers (remember that they need to be unique => use `set`)

## 🧪 Complexity

This problem is pretty straightforward. Everything scales linearly.

- **Time:** O(n)
- **Space:** O(n)

## 🔗 Leetcode Link

[Leetcode 3487](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/?envType=daily-question&envId=2025-07-25)