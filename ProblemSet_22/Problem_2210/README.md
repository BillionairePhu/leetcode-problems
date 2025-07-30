# 🔥 Leetcode Problem (2210)

> **Problem:** [Count Hills and Valleys in an Array](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`

---

### ✅ Intuition

Very intuitive problem. Just iterate through the number in the array and check its closest non-equal neighboring numbers to see if it is a hill or valley. But you need to take into account that there cases where multiple numbers are parts of a big hill/valley.

---

### 💡Implementation

Make a for loop iterate from the second number to the second number from the end (because the first and the last number cannot be a hill/valley - they do not have neighbors).

If the next number is equal to the current number, skip the current number - because the next check is enough to validate if the current number is a part of the hill/valley (plus we only wants to increase the result by 1 if many numbers are parts of the same hill/valley).

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)