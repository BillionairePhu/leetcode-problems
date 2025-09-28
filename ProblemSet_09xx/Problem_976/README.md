# 🔥 Leetcode Problem (976)

> **Problem:** [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `Math`, `Greedy`, `Sorting`

---

### ✅ Intuition

Sort the nums ascendingly and then assuming the 3 sides are `a`, `b`, `c` (`a <= b <= c`), we now just need to check three consecutive numbers starting from the back.

---

### 🧪 Complexity

- **Time:** O(n log(n))
- **Space:** O(n)