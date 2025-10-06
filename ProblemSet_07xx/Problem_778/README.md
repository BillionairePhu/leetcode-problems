# 🔥 Leetcode Problem (778)

> **Problem:** [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Array`, `Binary Search`, `Depth-First Search`, `Breadth-First Search`, `Union Find`, `Heap (Priority Queue)`, `Matrix`

---

### ✅ Intuition

To simplify the problem description: find minimum `t` such that with that `t`, we can go from the starting point `(0,0)` to the right corner `(m-1, n-1)`.

In other word, at time `t`, any cells that has the level value less than or equal to `t` is submerged and we can travel between any adjacent submerged cells => we need to expand from the starting cell to the right corner cell.

The trick here is very simple: we slowly increase the level of water `t` and put expanding cell-candidates into a small-heap. If the cell is submerged, we will add the neighboring cells into the heap. 

If the considered cell is the right corner cell, we break the loop and return the `t` value.

Repeat this step until the lowest-level cell is no longer submerged. Only then that we increase `t` and then repeat the step.

---

### 🧪 Complexity

- **Time:** $O(m*n log(m*n))$
- **Space:** $O(m*n)$