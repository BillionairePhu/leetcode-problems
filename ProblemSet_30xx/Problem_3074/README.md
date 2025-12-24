# 🔥 Leetcode Problem (3074)

> **Problem:** [Apple Redistribution into Boxes](https://leetcode.com/problems/apple-redistribution-into-boxes/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `Greedy`, `Sorting`

---

### ✅ Intuition

A very simple problem. We need to add up the largest capacities until it is more than the number of apples. And then the result is the number of capacities we have added.

---

### 💡Implementation

We can use either sorting or heap to have a list of largest capacities.

---

### 🧪 Complexity

Let N be the number of capacities and M be the number of boxes.

- **Time:** O(N * log(N) + M)
- **Space:** O(N)