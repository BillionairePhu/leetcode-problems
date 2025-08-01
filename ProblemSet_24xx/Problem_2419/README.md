# 🔥 Leetcode Problem (2419)

> **Problem:** [Longest Subarray With Maximum Bitwise AND](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Bit Manipulation`, `Brainteaser`

---

### ✅ Intuition

This is kind of a trick question :DD the largest bitwise AND value of any subarray is actually the largest number in the array.

Why? Because any result of a bitwise AND operation will always return a value that is smaller than its operands.

As a result, the problem can simplified as finding the longest subarray containing only the largest number.

---

### 💡Implementation

Use a max function to store the largest number `MAX` in the array. Use a variable `result` for storing the answer for the problem.

Iterate through the number and keep track of the number of `MAX` consecutive appearance. If the number of `MAX` consecutive appearances is larger than `result`, update `result` to it.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)