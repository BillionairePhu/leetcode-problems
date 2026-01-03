# 🔥 Leetcode Problem (1411)

> **Problem:** [Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Dynamic Programming`

<p>You have a <code>grid</code> of size <code>n x 3</code> and you want to paint each cell of the grid with exactly one of the three colors: <strong>Red</strong>, <strong>Yellow,</strong> or <strong>Green</strong> while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).</p>

<p>Given <code>n</code> the number of rows of the grid, return <em>the number of ways</em> you can paint this <code>grid</code>. As the answer may grow large, the answer <strong>must be</strong> computed modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/03/26/e1.png" style="width: 400px; height: 257px;" />
<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 12
<strong>Explanation:</strong> There are 12 possible way to paint the grid as shown.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5000
<strong>Output:</strong> 30228214
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
</ul>

---

### ✅ Intuition

We can notice that the color all have the same role so we can generalize the color without losing the accuracy. As a result, any combinations of a row (1 x 3) can be two-color combination *a x b x a* or three-color combination *a x b x c*.

The two-color row can allow 5 new combinations for the next row:
a b a
=>
b a b (2-color)
b a c (3-color)
b c b (2-color)
c a b (3-color)
c a c (2-color)

The three-color row can allow 4 new combinations for the next row:
a b c
=>
b a b (2-color)
b c a (3-color)
b c b (2-color)
c a b (3-color)

Using this piece of information, we can gradually calculate the number of combinations for `n` > 1.

---

### 💡Implementation

We create a loop for `n-1` time and keep track of the number of the grid option so far that ends at a `2-color` row and `3-color` row. At ech iteration, we calculate the options at the next row, also group by the 2 row types.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)