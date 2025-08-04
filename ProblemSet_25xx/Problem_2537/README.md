# 🔥 Leetcode Problem (2537)

> **Problem:** [Count the Number of Good Subarrays](https://leetcode.com/problems/count-the-number-of-good-subarrays/description/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Sliding Window`, `Hash table`

---

### ✅ Intuition

If a subarray from [i, j] is good then any subarrays [i, k] with k >= j is also good. With this in mind, we can implement a sliding window to calculate the number of "good" subarrays. (*)

We will have 2 variables `start` and `end` to keep track of the smallest "good" subarrays ending at `end`. Also, we will have a variable `comb_count` to keep track of the current index pairs satisfying the problem.

We iterate `end` from index 0 to the last index of the array and calculate new `comb_count`. If the `comb_count` is larger or equal to `k` then the subarray from `start` to `end` is a "good" subarray (smallest "good" subarray ending at `end`). We will add the number of indices after or equal to `end` to the result because of the property at (*). After that, increase `start` and calculate the new `comb_count`. Repeat until `comb_count` is no longer larger or equal to `k`

---

### 💡Implementation

For the calculation of `comb_count`, we will use a hash table to store the count of each number while iterating and use combination formula to update `comb_count`

Use sliding window of `start` and `end` to iterate through all possible results.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)