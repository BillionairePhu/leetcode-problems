# 🔥 Leetcode Problem (1493)

> **Problem:** [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Dynamic Programming`, `Sliding Window`

---

### ✅ Intuition

In other words, the problem asks us to find the longest subarray with at most one zero inside it. This sounds very similar to a sliding window problem.

---

### 💡Implementation

Keep track of the left and right boundary of the sliding window and increment the right boundary.

For each increment, check if there is at most one zero in the subarray bounded by the sliding window. If not, we will increment the left boundary until there are at most one zero.

Remember to keep track of the length of the sliding window as the result is equal to the maximum length - 1

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)