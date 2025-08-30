# 🔥 Leetcode Problem (36)

> **Problem:** [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Matrix`

---

### 💡Implementation

Since you need to check if a value is already existed in the same row/column/sub-square, it's best to use a set to store the values in each row/column/sub-square.

Then iterate through each cell and check if its value is already in the corresponding sets, if not then add that value to the sets.

In the end, return true if there is no cell having duplicated value.

---

### 🧪 Complexity

The algorithm needs to go through each cell in the sudoku table (81 cells).

- **Time:** O(81)