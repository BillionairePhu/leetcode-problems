# 🔥 Leetcode Problem ({{ frontendQuestionId }})

> **Problem:** [Trapping Rain Water II](https://leetcode.com{{ link }})<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Breadth-first search`, `Heap`

---

### Overview

We are given a grid, heightMap, where each element represents the height of the corresponding cell in the 3D representation of the map. Our task is to calculate the total amount of water trapped on the map after it rains.

We can assume that it rains an infinite amount of water, but the water stays inside any area of the map only if there is a boundary that traps it. Specifically, the water remains on top of a cell as long as its combined height (the height of the cell plus the water above it) is less than or equal to the height of all its neighbors. If any neighbor is lower, the water will flow out to that lower cell.

Approach: BFS + Priority Queue

---

### Intuition

Building on the earlier observation, the total height of any cell (its original height plus any trapped water) must not exceed the smallest total height of its neighbors. Specifically, it cannot exceed the smallest total height of its neighboring cells. This constraint propagates outward from the grid’s edges, which act as the ultimate boundary since no water can be trapped beyond them.

In simpler terms, the cells around a region of the grid act as a boundary, and the smallest height of this boundary determines how much water can be stored in that region. To solve the problem, we begin by treating the edges of the grid as the initial boundary since water cannot spill beyond them. From there, we move inward, processing cells in a manner that respects the relationship between a cell’s height and the boundary:

Trapping Water: When we process a cell, if its height is lower than the current boundary height, water can be trapped above it. The amount of water trapped is equal to the difference between the boundary height and the cell’s height. We then add this trapped water to our running total. To ensure the boundary remains valid, the cell is added to the boundary with its effective height adjusted to match the current boundary height. This adjustment prevents water from "spilling" through this cell and invalidating the boundary.

Updating the Boundary: If the cell's height is greater than or equal to the boundary height, no water can be trapped above it. However, the cell still becomes part of the boundary because it might help trap water in adjacent, higher regions as we continue processing.

To efficiently manage the boundary and dynamically update the smallest height, we use a min-heap (priority queue). The heap lets us quickly find the lowest boundary height and ensure the traversal always processes the most constrained regions first.

For a more comprehensive understanding of heaps and priority queues, check out the Heap Explore Card 🔗. This resource provides an in-depth look at heap-based algorithms, explaining their key concepts and applications with a variety of problems to solidify understanding of the pattern.

---

### 🧪 Complexity

Let `k = m*n` be the total number of cells in the grid

- **Time:** O(k * log k)
- **Space:** O(k)