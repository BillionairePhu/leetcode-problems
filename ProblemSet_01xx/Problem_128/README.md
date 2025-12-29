# 🔥 Leetcode Problem (128)

> **Problem:** [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Union Find`

<p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,2]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

---

### ✅ Intuition

Since the problem only allow O(n) time complexity for the array, the solution must use a HashSet<> or Dictionary<,>. For this to work, we must know ahead of time what information we need when adding a number. Imagine adding one more number k, if k already exists, then adding it does nothing. Adding k either add a new sequence \[k, k\] or modifies existing ones. If k were to modify a sequence \[a, b\], then either k = a - 1 or k = b + 1. Hence, it would be suffient to store at both end of the sequence, the sequence itself to know how a sequence change.

---

### 💡Implementation

*Add your notes or explanation here.*

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)