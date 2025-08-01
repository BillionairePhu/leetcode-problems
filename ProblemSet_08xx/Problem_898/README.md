# 🔥 Leetcode Problem (898)

> **Problem:** [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Dynamic Programming`, `Bit Manipulation`, `Hashed Table`

---

### ✅ Intuition

Use set `result` to keep track of unique values obtained from bitwise ORs of subarrays.

The problem basically asks us to count all the unique values. We can see from the constraints that this problem should have a complexity of `O(n^2)` so the idea would be to have a loop within a loop.

So first, we iterate through the number in the arrays and use another set `currSet` to keep track of the xor results ending at the current index.

In each iteration, we take each value in `currSet` and do bitwise OR with the current value and then add to the `result` set. Remember to also add the current number to the `result` set for each iteration.

---

### 🧪 Complexity

- **Time:** O(n^2)
- **Space:** O(n`)