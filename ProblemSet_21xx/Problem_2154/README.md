# 🔥 Leetcode Problem (2154)

> **Problem:** [Keep Multiplying Found Values by Two](https://leetcode.com/problems/keep-multiplying-found-values-by-two/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `Hash Table`, `Sorting`, `Simulation`

---

### ✅ Intuition

Have a loop and for each iteration, we check if the `original` number is in the list of numbers. If it is in, multiply by 2 and assign it to `original` and do the loop again; else return `original`.

---

### 💡Implementation

We can use a set to check if the `original` number in the list in O(1) time

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)