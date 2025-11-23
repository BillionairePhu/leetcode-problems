# 🔥 Leetcode Problem (1262)

> **Problem:** [Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Dynamic Programming`, `Greedy`, `Sorting`

---

### ✅ Intuition

We can find the "Greatest Sum Divisible by Three" by finding the sum of all elements in the array, and then try to remove some elements until the sum is divisble by 3 (minimizing the removed value).

There are 3 scenarios for the total sum:

- modulo 3 = 0: the simplest scenario, the sum is divisble by 3 and thus we just need to return the totatl sum
- modulo 3 = 1: we need to remove 1 number that modulo 3 = 1 or 2 numbers that modulo 3 = 2 (whatever is smaller)
- modulo 3 = 2: we need to remove 1 number that modulo 3 = 2 or 2 numbers that modulo 3 = 1 (whatever is smaller)

To do the actions in the later scenarios, we need to track of 2 smallest numbers for each modulo value.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)