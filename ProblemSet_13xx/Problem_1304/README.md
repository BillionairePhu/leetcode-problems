# 🔥 Leetcode Problem (1304)

> **Problem:** [Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `Math`

---

### ✅ Intuition

Just append each pair of opposite-sign numbers so that the total sum is 0. But remember that the numbers need to be unique so you cannot use the same number twice => the easy easiest way is to increment the number being used.

If `n` is odd -> then there is a number not having the opposite-sign number => just use 0

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)