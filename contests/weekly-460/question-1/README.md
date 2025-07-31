# 🔥 Problem (Weekly 460)

> **Problem:** [Maximum Median Sum of Subsequences of Size 3](https://leetcode.com/contest/weekly-contest-460/problems/maximum-median-sum-of-subsequences-of-size-3/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Math`, `Array`

---

### ✅ Intuition

Fairly easy question. You just need to realize that the maximum median sum is the sum of all number at index `(n + 2*i)` with i in range [0, n-1]

#### Why is that?

First, because we can pick any three numbers at a time, so the order of the picked number is not important. As a result, we should sort the list ascendingly so that we can keep track which number is larger than which number.

As a result, the problem becomes: do `n` times (pick and erase 1 number `x` to add to the result, then erase `y` and `z` such that `y` is smaller than `x` and `z` is larger than `x`).

=> Straightforward, since we have to erase `n` numbers `y < x`, these `y`s should be the smallest numbers (because we want to maximize the result -> eliminate all small numbers).

Now, we are left with `2*n` numbers at indices from `n` to `3*n-1`, of these numbers, we need to pick `n` `x`s to add to the result and `n` `z`s to eliminate such that `z > x`.

This is tricky. The key is to realize that to get the maximum sum, we need to eliminate the minimum numbers. As a result, for any number `x` at index `i` we pick, we should eliminate the very next number `z` at index `i+1`.

Tada, the result will be  all number at index `(n + 2*i)` with i in range [0, n-1]

---

### 💡Implementation

- Sort the array

- Initialize `result` to store the result value and add any numbers at index `(n + 2*i)` with i in range [0, n-1]

---

### 🧪 Complexity

There are two steps in this solution: sort and iterate. Since iterating only has linear time complexity and constant space complexity, sorting is clearly more complex. As a result, the complexity will depends on the complexity of the sort function (which - for the sake of this solution - is Python's default sorting Timsort).

- **Time:** O(n*log(n))
- **Space:** O(n)