# 🔥 Leetcode Problem (3228)

> **Problem:** [Maximum Number of Operations to Move Ones to the End](https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `String`, `Greedy`, `Counting`

---

### ✅ Intuition

We can notice that: in order to maximize the number of operations, we would prioritize doing operation for the leftmost operatable `1` because then moving the next `1` could create a gap so that we could move the previous `1` once again.

In addition, we can generalize the maximum number of operations a `1` can do is:

- `k + 1` if there is a `0` between it and the nearest `1` to its right 
- `k` if there is no `0` between it and the nearest `1` to its right 

with `k` being the maximum number of operations the nearest `1` to the right can do.

---

### 💡Implementation

We can do a loop from right to left and dynamically calculate the number of operations for each `1`

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)