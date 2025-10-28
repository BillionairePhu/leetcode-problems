# 🔥 Leetcode Problem (1716)

> **Problem:** [Calculate Money in Leetcode Bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Math`

---

### ✅ Intuition

Just do the simulation by having a variable to keep track of the input `money` on Monday of the current week (after each week, increment `money` by 1). For each day, we will add to `result` the amount of `money` on Monday plus the day from Monday.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)