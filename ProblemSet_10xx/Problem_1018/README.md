# 🔥 Leetcode Problem (1018)

> **Problem:** [Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `Bit Manipulation`

---

### ✅ Intuition

Simple problem. We just need to loop through the array and calculate the new number + the modulo to see if the new number is divisible by 5.

There is only one problem, if we keep calculating the new number, we will soon run out of memory to store number because the upper range would be 2^10000. The trick is to only keep the modulo in the memory and calculate based on that.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)