# 🔥 Leetcode Problem (3623)

> **Problem:** [Count Number of Trapezoids I](https://leetcode.com/problems/count-number-of-trapezoids-i/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Math`, `Geometry`

---

### ✅ Intuition

Since the probably on asked for "horizontal" trapezoid, there must always be 2 pairs of points on the same line.

Let's say on the horizontal line of `y=a`, there are `k` points, then there will be `kC2` selections possible. We can do this for every single horizontal line and got the number of selections at each line.

For 2 distinct horizontal lines, the number of trapezoids would be `kC2` times `hC2`.

As a result, to calculate the total number of trapezoids, we will get the product of selections at each pair of horizontal line.

A trick to fast-track this would be to compute the sum of all selections and iterate through each row's selection.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)