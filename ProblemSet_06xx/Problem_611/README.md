# 🔥 Leetcode Problem (611)

> **Problem:** [Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Two Pointers`, `Binary Search`, `Greedy`, `Sorting`

---

### ✅ Intuition

To do this problem, we need to know what constraints the sides of a triangle needs to follow. There is actually one: of 3 sides of a triangle, any 2 side must have lengths summing up larger than the remaining side.

There are approaches we can use: brute-force or sorting.

Basically, brute-force is trying every triplet of side and checking if they make a valid triangle.

On the other hand, we can sort the array of sides first. And then we iterate two pointers `i`, `j` with `i` < `j`, they are the indices of the two smaller sides of the triangle. For each pair, we can find the number of `k` that makes valid triangle (`i` < `j` < `k`) just by finding out starting from which index back to `j` that the triangle with those indices will be valid.

---

### 🧪 Complexity

- **Time:** O(n^2)
- **Space:** O(n)