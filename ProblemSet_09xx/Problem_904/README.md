# 🔥 Leetcode Problem (904)

> **Problem:** [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Sliding Window`

---

### ✅ Intuition

Since we have 2 baskets and each basket can contain at most one type of fruit, we can only have at most 2 types of fruits at one time. There is also this constraint: `Once you reach a tree with fruit that cannot fit in your baskets, you must stop.`. Conveniently, this limits to only pairs of 2 consecutive unique fruits.

We just need to iterate from left to right and keep track of the number of fruits can be added with the given constraints. Actually this makes that, at any time, there are only 2 options to keep track of.

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)