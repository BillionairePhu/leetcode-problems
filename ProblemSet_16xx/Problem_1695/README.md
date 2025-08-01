# 1695. Maximum Erasure Value

Tag: `Sliding Window`

Link: [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/description/?envType=daily-question&envId=2025-07-22)

## Intuition

We can see that a valid subarray is like a window and the numbers in these window must be unique (no duplication). Therefore, we can use a set to check if there is any duplication.

If we want to extend the window and there is already a number in the set, we must try to reduce the set.

## Approach

Use variables to store the final result `result`, the current sum `sum` and a set `myset` to store which number is present in the array.

Why we want use set instead of array? Because the action of checking if a number in a set has complexity O(1) while doing that for an array has a complexity O(k) with k being the number of elements in the array.

Iterate the right point of the window from left to right. For each iteration, check if there is already the new number in the window; if so, slide the left point until there is only one instance of that number. Then update the result if the sum of the numbers in the window is greater than the current result.
