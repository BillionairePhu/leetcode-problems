# 🔥 Leetcode Problem ({{ frontendQuestionId }})

> **Problem:** [Minimum Cost Homecoming of a Robot in a Grid](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/description/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Greedy`

---

### ✅ Intuition

This should be an easy challenge. The key here is to realize that the lowest-cost path from start to home is to go directly to it. There is no workaround that lower the costs!!!

---

### 💡Implementation

Due to the key realization mentioned above, we just need to calculate the cost of moving directly once between the rows and columns in-between start and home. Two simple for loops should be sufficient for this task.

---

### 🧪 Complexity

Let `m` be the number of rows of this problem and `n` be the number of columns of this problem

- **Time:** O(m + n)
- **Space:** O(1)