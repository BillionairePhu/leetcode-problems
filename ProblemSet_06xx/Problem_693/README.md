# 🔥 Leetcode Problem (693)

> **Problem:** [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Bit Manipulation`

<p>Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> The binary representation of 5 is: 101
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> false
<strong>Explanation:</strong> The binary representation of 7 is: 111.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> false
<strong>Explanation:</strong> The binary representation of 11 is: 1011.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

---

### ✅ Intuition

Just simply check do what the problem asks: check if all consecutive bit is of different state (on/off)

---

### 💡Implementation

Do a while loop and shift right the number gradually to iterate through the bit from right to left. To get the state of the current bit, just do a BIT-wise `AND` between the current number and `1`, then compared it with the previous state (we should keep track of the previous state by storing in a variable `state`). After each iteration, update the state.

If there exists just one pair not satisfying the condition, break and return False. If not, return True.

---

### 🧪 Complexity

Let `n` be the number of bit in the binary representation of the number.

- **Time:** O(log n)
- **Space:** O(1)