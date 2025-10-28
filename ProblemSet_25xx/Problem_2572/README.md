# 🔥 Leetcode Problem (2572)

> **Problem:** [{{ title }}](https://leetcode.com{{ link }})<br />
> **Difficulty:** {{ difficulty }}<br/>
> **Tags:** {% for tag in topicTags %}`{{ tag.name }}`{% if not loop.last %}, {% endif %}{% endfor %}

---

### ✅ Intuition

Very interesting problem, however, the solution for the problem can only be applicable for small constraints (`nums[i] <= 30`).

To do this, we will use dynamic programming techniques - calculating the number of subsets if there are only `i` first numbers in the array. But we need to keep track of the frequencies of product values of these subset because they can affect the next dynamic programming result.

To better keep track of the frequencies, we will not use the key being the product value itself but rather using the bitmask with each bit representing the appearance of a prime factor in the product.

---

### 🧪 Complexity

- **Time:** O(n * 10)
- **Space:** O(10)