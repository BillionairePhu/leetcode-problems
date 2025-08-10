# 🔥 Leetcode Problem (869)

> **Problem:** [Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Hash Table`, `Math`, `Sorting`, `Counting`, `Enumeration`

---

### ✅ Intuition

I think the key point in this problem is realizing that there are only 30 power-of-2 numbers that is less than 10**9 (the upper constraints). As a result, you just need to check if the current number contains the digits of any power-of-2.

---

### 💡Implementation

Loop through the first 30 power-of-2 and store their `Counter` in a constraint.

Calculate the `Counter` of the current number and check if match any of the stored counters.

---

### 🧪 Complexity

For this problem, the complexity is the number of power-of-2 needs to be checked.

- **Time:** O(30)
- **Space:** O(30)