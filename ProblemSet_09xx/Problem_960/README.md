# 🔥 Leetcode Problem (960)

> **Problem:** [Delete Columns to Make Sorted III](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Array`, `String`, `Dynamic Programming`

---

### ✅ Intuition

We can use dynamic programming for this problem with `dp[i]` being the maximum number of columns can be kept that is valid and ending with the column `i`.

Using this, we have this formula: if a column `j` (`j < i`), `dp[i]` could be `dp[j] + 1` if for every strings, the character at index `i` is larger than or equal to the character at index `j`. The idea for this formula is that the column right before column `i` could be column `j` => `dp[i]` could be `dp[j] + 1`

---

### 💡Implementation

We use 3 nested loops to solve this problem:

- The outer loop would be to solve for `dp[i]`
- The middle loop would be to check for each `j` if it is valid for the corresponding `i`
- The inner loop would be to check if all `string`s can satisfy that character at `i` is larger than or equal to character at `j`.

---

### 🧪 Complexity

Let M be the number of column and N be the number of string in `strings`

- **Time:** O(M^2 * N)
- **Space:** O(M)