# 🔥 Leetcode Problem (1975)

> **Problem:** [Maximum Matrix Sum](https://leetcode.com/problems/maximum-matrix-sum)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Greedy`, `Matrix`

<p>You are given an <code>n x n</code> integer <code>matrix</code>. You can do the following operation <strong>any</strong> number of times:</p>

<ul>
	<li>Choose any two <strong>adjacent</strong> elements of <code>matrix</code> and <strong>multiply</strong> each of them by <code>-1</code>.</li>
</ul>

<p>Two elements are considered <strong>adjacent</strong> if and only if they share a <strong>border</strong>.</p>

<p>Your goal is to <strong>maximize</strong> the summation of the matrix&#39;s elements. Return <em>the <strong>maximum</strong> sum of the matrix&#39;s elements using the operation mentioned above.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png" style="width: 401px; height: 81px;" />
<pre>
<strong>Input:</strong> matrix = [[1,-1],[-1,1]]
<strong>Output:</strong> 4
<b>Explanation:</b> We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png" style="width: 321px; height: 121px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
<strong>Output:</strong> 16
<b>Explanation:</b> We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 250</code></li>
	<li><code>-10<sup>5</sup> &lt;= matrix[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

---

### ✅ Intuition

We can imagine that the negative numbers in the matrix are black dots, we can move the black dots to anywhere (`Choose any two adjacent elements of matrix and multiply each of them by -1.`) and in the end, there will be at most 1 last dot (any two dots can cancel themselves by moving them next to each other and multiply both by -1).

- *In the case that there is a zero anywhere in the matrix*, we move the last black dot next to the zero and multiply both by -1, thus there will be zero black dot. => The result will be the sum of absolute value of all matrix elements.

- *If not*, we can move the final black dot to the element with the smallest absolute level => The result will be the negative value of that selected element plus all other elements' absolute values. 

---

### 💡Implementation

Just make a simple nested loop to go through all element and check the above condition + calculate the minimum absolute value and the total value of all elements' absolute values.

---

### 🧪 Complexity

- **Time:** O(N x M)
- **Space:** O(1)