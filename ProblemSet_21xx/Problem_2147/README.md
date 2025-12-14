# 🔥 Leetcode Problem (2147)

> **Problem:** [Number of Ways to Divide a Long Corridor](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Math`, `String`, `Dynamic Programming`

---

### ✅ Intuition

This is actually an easy problem, you just need to use combinatory math to solve it.

For this problem, the number of dividers is actually a constant (`(n_s - 2) / 2`) because all spaces between 2 dividers must have 2 seats. And for each divider, you can only have `k_i` options, which can be calculated based on the number of plants between 2 consecutive spaces' right-most and left-most seats.

Also, remember to check if the number of seats are even => else there is no way to put the divider.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)