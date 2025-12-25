# 🔥 Leetcode Problem (169)

> **Problem:** [Majority Element](https://leetcode.com/problems/majority-element)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `Hash Table`, `Divide and Conquer`, `Sorting`, `Counting`

<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The input is generated such that a majority element will exist in the array.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?
---

### ✅ Intuition

This problem asks us to find the number that appears more than N/2 times.

#### Naive method

The naive ways would be storing the appearances of different numbers in a hashed table. Then iterate through the array and increment the corresponding appearance count. Finally, we return the number with the most appearances.

*The naive method takes O(N) time and O(N) space*

#### Boyer-Moore voting algorithm

Another way to solve this is to use Boyer-Moore voting algorithm. Since we know that there exists a majority number (more than N/2) times. We can set up a voting mechanism such that:
- When we iterate through the element, we will increment the `maj_count` if the current number is the same as the current majority number. If not, we decrease the current majority number's count and replace it with the current number if it drops below 0.
- The majority number at the end of the iteration will be the final result

**Why does this work?**

It works because if there exists a number with appearance more than N/2, its appearances in the array will always overwrite any other numbers eventually.

> Actually, we can confirm if that number is actually the majority (more than N/2) by iterating one more time and counting the appearance of that number.

*The Boyer-Moore voting algorithm will take O(N) time and O(1) space*
