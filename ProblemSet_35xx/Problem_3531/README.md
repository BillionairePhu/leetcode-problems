# 🔥 Leetcode Problem (3531)

> **Problem:** [Count Covered Buildings](https://leetcode.com/problems/count-covered-buildings/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Sorting`

---

### ✅ Intuition

First, pre-process the data, for every row and column having a building, keep track of the left/right-most or top/bottom-most building.

Then iterate through the buildings and check if the building is on any side based on the pre-processed data.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)