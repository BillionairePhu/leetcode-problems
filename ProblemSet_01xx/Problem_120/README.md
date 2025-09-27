# 🔥 Leetcode Problem (120)

> **Problem:** [Triangle](https://leetcode.com/problems/triangle/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Dynamic Programming`

---

### ✅ Intuition

This problem asks us to implement accessing matrices' cells based on its description. The logic is very simple: from top down, the current cell at row `i` column `j` will increment by the min value of the two cells above it (on row `i-1` and columns `j-1` or `j`).

---

### 🧪 Complexity

With n being the number of rows, the complexity is O(n^2) - which scales with the number of cells being processed. Since we write directly to the given matrix, we only need constant memory.

- **Time:** O(n^2)
- **Space:** O(1)