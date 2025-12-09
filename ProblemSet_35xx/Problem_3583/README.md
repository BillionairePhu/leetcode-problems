# 🔥 Leetcode Problem (3583)

> **Problem:** [Count Special Triplets](https://leetcode.com/problems/count-special-triplets/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Counting`

---

### ✅ Intuition

We keep track of a `result` variable (starting at 0) and then iterate through each number `j` (from 0 to `n-1`). At each iteration, we calculate the number of valid triplets by incrementing `result` by the appearances of `nums[j]*2` on the left multiplied with the appearances of `nums[j]*2` on the right.

To know the appearances of a number on the left and on the right, we use two hash tables: `left_counter` and `right_counter`. The left counter is calculated up when iterating, and the right counter is the appearances of all numbers calculated down when iterating.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)