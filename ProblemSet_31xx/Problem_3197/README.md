# 🔥 Leetcode Problem (3197)

> **Problem:** [Find the Minimum Area to Cover All Ones II](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Array`, `Matrix`, `Enumeration`

---

### ✅ Intuition

Quite difficult challenge. You need to check all the possibilities to find the solution :v that's why the constraints of this problem is `1 <= grid.length, grid[i].length <= 30` - relatively small.

The idea here is for any two rectangles, there is either a horizontal line or a vertical line that separates the grids into 2 zones, each contains one rectangle.

As a result, we can try splitting the grid into two areas and finding the smallest rectangle in each area to cover all ones. => by doing this, we have solved for the case there are 2 rectangles. For 3 rectangles, we can break down one of the two divided areas into two => now we have 3 areas, we just need to find the smallest rectangle for each area.

To find the smallest rectangle for each area, we just need to find the leftmost, rightmost, topmost and bottommost one in each area.

---

### 💡Implementation

Use recursion with a variable `shapes` and a base case when `shapes` is one to recursively divides the grid into smaller areas. Then calculate the sum of all rectangles in each case => keep track of the smallest sum (the answer).

---

### 🧪 Complexity

- **Time:** O(n^4)
- **Space:** O(1)