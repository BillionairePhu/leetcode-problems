# 🔥 Leetcode Problem (37)

> **Problem:** [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Array`, `Hash Table`, `Backtracking`, `Matrix`

---

### ✅ Intuition

First we need to find the list of possible values for each cell. This can be done by getting the existed values in the cell's row, column and sub-square; the possible values are the remaining values that are existed yet.

Then, we will try each value in the cell, one after another. If there exists no valid sudoku answer for that value, we backtrack to the previous cell and try another possible value.
