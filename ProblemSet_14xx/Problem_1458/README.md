# 🔥 Leetcode Problem (1458)

> **Problem:** [Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Array`, `Dynamic Programming`

<p>Given two arrays <code>nums1</code>&nbsp;and <code><font face="monospace">nums2</font></code><font face="monospace">.</font></p>

<p>Return the maximum dot product&nbsp;between&nbsp;<strong>non-empty</strong> subsequences of nums1 and nums2 with the same length.</p>

<p>A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie,&nbsp;<code>[2,3,5]</code>&nbsp;is a subsequence of&nbsp;<code>[1,2,3,4,5]</code>&nbsp;while <code>[1,5,3]</code>&nbsp;is not).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,1,-2,5], nums2 = [3,0,-6]
<strong>Output:</strong> 18
<strong>Explanation:</strong> Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [3,-2], nums2 = [2,-6,7]
<strong>Output:</strong> 21
<strong>Explanation:</strong> Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [-1,-1], nums2 = [1,1]
<strong>Output:</strong> -1
<strong>Explanation: </strong>Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 500</code></li>
	<li><code>-1000 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

---

### ✅ Intuition

For each index <code>i</code>, store <code>m[i]</code> as the max dot product from the start to <code>i</code>. Then the max dot product is <code>m[^1]</code> (last index).

If a new value <code>v</code> is added to an array, for instance <code>nums1</code>, the max dot product from the start to <code>i</code> after adding is either <code>pm[i - 1]</code>, <code>nums2[i] * v + pm[i - 1]</code> where <code>pm</code> is the previous max ... or the current max from the start to <code>i - 1</code>.


### 🧪 Complexity

- **Time:** O(n * m)
- **Space:** O(m)