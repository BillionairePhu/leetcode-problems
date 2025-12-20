# 🔥 Leetcode Problem (944)

> **Problem:** [Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `String`

---

### ✅ Intuition

Check column by column to find how many columns are not sorted lexicographically.

For each column, we will iterate through the strings and check the character at `column` index to see if it is in-order.

---

### 🧪 Complexity

- **Time:** O(n*m)
- **Space:** O(1)