# 🔥 Leetcode Problem (3542)

> **Problem:** [Minimum Operations to Convert All Elements to Zero](https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Stack`, `Greedy`, `Monotonic Stack`

---

### ✅ Intuition

The rule here is that whenever you do an operation on a subarray, it will turn all appearances of the minimum number to 0. Thus, this operation will create isolation area (i.e. after performing operation on [a,b], it is meaning less to perform an operation on [c,d] such that c <= a and d >= b) because the minimum of any subarrays containing the already-processed subarray will be 0.

If it is still too hard to understand, imagine this! We have the following "hill" of number:

- 1, 3, 5, 3, 1

If we process number subarray bounding by number 3 first, the resulting array would become 1, 0, 5, 0, 1. The processed position (number 3) will become the points of isolation because it turns into 0 and thus any new operations containing the isolation position is meaningless (cannot decrease number anymore).

As a result, when doing an operation, we need to try wider subarrays first and then move to smaller subarrays to not introduce many isolation points too early.

Ok, that's the point. But considering each subarray until everything is 0 has a great complexity of O(n^2), that cannot be the solution.

The solution here is to use stack! We can notice that moving from left to right, whenever we hit a local minimum, that must be a point of isolation and the previous subarray from the previous minimum to it is isolated. That's the key!!! Whenever we hit a local minimum, process the previous isolated subarray.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)