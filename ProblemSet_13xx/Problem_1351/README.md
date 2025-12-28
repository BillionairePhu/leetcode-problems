# 🔥 Leetcode Problem (1351)

> **Problem:** [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `Binary Search`, `Matrix`

<p>Given a <code>m x n</code> matrix <code>grid</code> which is sorted in non-increasing order both row-wise and column-wise, return <em>the number of <strong>negative</strong> numbers in</em> <code>grid</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 8 negatives number in the matrix.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[3,2],[1,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-100 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you find an <code>O(n + m)</code> solution?
---

### ✅ Intuition

*Add your notes or explanation here.*

---

### 💡Implementation

For each row, we find the index `i` of the first negative number in the row (if there is no negative number `i` is N, *the length of the row*). Then, that row will have `N - i` negative number. The most optimal way to do this in a sorted row is using binary search (`bisect` in Python).

Since the matrix is also sorted non-increasing column-wise, we know that in the next row at index `i`, the number will also be negative. Then we will check its left neighbor, if that number is also negative then `i`-th number is not the first negative number in the row. So we decrement `i` and do this check again until the number on the left of `i` is a non-negative number or `i` equals 0.

After calculating for all rows, the result is the sum of all rows' results.

---

### 🧪 Complexity

- **Time:** O(N + M + log(N))
- **Space:** O(1)