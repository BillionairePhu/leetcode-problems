# 🔥 Leetcode Problem (417)

> **Problem:** [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Depth-First Search`, `Breadth-First Search`, `Matrix`

---

### ✅ Intuition

This is an expanding-search problem, you can use either depth-first or breadth first. The key is finding all the cells that could be expanded from the Pacific and all the cells that could be expanded from the Atlantic. The answer to this problem are the cells overlapped by these 2 groups.

---

### 🧪 Complexity

- **Time:** O(m*n)
- **Space:** O(m*n)