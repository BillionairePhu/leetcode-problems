# 🔥 Leetcode Problem (3652)

> **Problem:** [Best Time to Buy and Sell Stock using Strategy](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Sliding Window`, `Prefix Sum`

---

### ✅ Intuition

Typical sliding window problem. We can notice that since the modification range is continous, it is actually a sliding window. We can iteratively move the window from left to right and calculate the profit of all prices.

---

### 💡Implementation

Set up a `window_profit` being the profit if the window is at the left-most. Then iteratively move the windows to the right until it hits the end, for each iteration, we need to recalculate the profit by adding/substracting prices affected by the movement.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)