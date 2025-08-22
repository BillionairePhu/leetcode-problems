# 🔥 Leetcode Problem (1277)

> **Problem:** [Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Dynamic Programming`, `Matrix`

---

### ✅ Intuition

The number of squares ending at an index (i, j) is the size of the largest square ending at that index.

There is a property here, a square of size `n` ending at index (i, j) is only possible if there exists squares of size `n-1` ending at (i-1, j), (i, j-1) and (i-1, j-1). Using this property, we can build a dynamic programming algorithm to get the size of the largest square ending at each index.

The result will be the sum of the sizes at the indices.

---

### 🧪 Complexity

- **Time:** O(n^2)
- **Space:** O(n^2)