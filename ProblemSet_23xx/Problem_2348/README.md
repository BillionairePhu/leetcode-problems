# 🔥 Leetcode Problem (2348)

> **Problem:** [Number of Zero-Filled Subarrays](https://leetcode.com/problems/number-of-zero-filled-subarrays/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Math`

---

### ✅ Intuition

> A subarray is a contiguous non-empty sequence of elements within an array.

We can solve this problem by counting the number of zero-filled subarrays ending at each index and then take the sum of it.

---

### 💡Implementation

Iterate through the number in the given array. Keep track of the number of consecutive zeros ending at the current index and add the number to the result each time we visit a zero number.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)