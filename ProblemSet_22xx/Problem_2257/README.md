# 🔥 Leetcode Problem (2257)

> **Problem:** [Count Unguarded Cells in the Grid](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Matrix`, `Simulation`

---

### ✅ Intuition

Simple simulation problem. For every guard, just mark its guarded cell with a certain value (follow the rule of wall) and then count the remaining unguarded cell.

---

### 🧪 Complexity

- **Time:** O(m*n)
- **Space:** O(m*n)