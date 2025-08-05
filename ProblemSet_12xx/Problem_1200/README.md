# 🔥 Leetcode Problem ({{ frontendQuestionId }})

> **Problem:** [Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/description/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Sorting`, `Array`

---

### ✅ Intuition

Just sort the array ascendingly and iterate through each consecutive pair. If the difference of that pair is smaller than minimum, reset the result array to store that pair; if equal, append to the result array; else, ignore.

---

### 🧪 Complexity

- **Time:** O(n * log n)
- **Space:** O(n)