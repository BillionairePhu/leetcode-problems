# 🔥 Leetcode Problem (118)

> **Problem:** [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `Dynamic Programming`

---

### ✅ Intuition

Pretty simple array problem. Just iterate through each row and for each row, calculate each number of it based on the previous row.

Another way would be using binomial coefficient.

### 🧪 Complexity

The complexity is actually based on the number of values in the result, which is quite easy to calculate `n * (n+1)/2` ~ O(n^2).

- **Time:** O(n^2)
- **Space:** O(n^2)