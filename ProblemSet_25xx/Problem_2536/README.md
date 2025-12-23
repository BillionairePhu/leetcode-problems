# 🔥 Leetcode Problem (2536)

> **Problem:** [Increment Submatrices by One](https://leetcode.com/problems/increment-submatrices-by-one/description/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Matrix`, `Prefix Sum`

---

### ✅ Intuition

Ah, this is a very intriguing question and let you implement a 2D prefix sum.

We can imagine that for each query, we will we have 2 cells `point1` (`row1`, `col1`) and `point2` (`row2`, `col2`). The cells within these 2 points will have their values increment by 1.

We can use a `diff` array to mark the area which values are manipulated. For any value in `diff`, it is understood that the area to the right and to the bottom of it would be affected. As a result, when processing each query, we will modify 4 cells in it:
- The top left one (1): marks the beginning of the affected area.
- The bottom left & the top right one (2 & 3): marks the end of the affected area
- The bottom right one (4): marks the very opposite end of the affected area.
Since the modified area of each value in `diff` is to the bottom and right, we will increment cells 1 & 4 while decrement cells 2 & 3 (because decrementing cells 2 & 3 would create an overlapping decrementing area from cell 4 so we need to increment at cell 4)

After processing all query, we will construct the values for each cell in our result matrix with the formula:

`M[i][j] = M[i-1][j] + M[i][j-1] - M[i-1][j-1] + diff`

Visualize this by imagining that each cell value is the result of being affected by all cells to the left and to the top of it.

---

### 🧪 Complexity

- **Time:** O(N*N + M)
- **Space:** O(N*N)