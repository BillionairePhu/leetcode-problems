# 🔥 Leetcode Problem (2044)

> **Problem:** [Count Number of Maximum Bitwise-OR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Backtracking`, `Bit Manipulation`, `Enumeration`

---

### ✅ Intuition

The maximum bitwise OR value obtained from any subsets of the array would be the value resulting from OR-ing all numbers in the array.

Then the naive method is to checking every combination of elements in the array to see if they all OR to the max value. To further optimize, we can use a backtrack function with prunning condition: if a subset or-ing equal to max, adding any elements to it will have bitwise OR equal to max.

---

### 🧪 Complexity

- **Time:** O(2^n)
- **Space:** O(n)