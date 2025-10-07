# 🔥 Leetcode Problem (1488)

> **Problem:** [Avoid Flood in The City](https://leetcode.com/problems/avoid-flood-in-the-city/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Binary Search`, `Greedy`, `Heap (Priority Queue)`

---

### ✅ Intuition

We need to consider how to selectively drain lakes when a flood is about to occur. To do this, we use an ordered set st to store days without rain. These sunny days can be used to drain lakes selectively when a flood is imminent, thus preventing it. The ordered set st maintains sunny days in increasing order of their indices, ensuring that we always perform the drainage operation on the earliest possible sunny day to maximize flood prevention.

For the remaining sunny days at the end, we can drain any arbitrary lake; for convenience, we choose lake 1.

We initialize an answer array ans of the same size as rains and set all values to 1. Then we traverse the rains array from left to right:

If rains[i]=0, we add i to the ordered set st.
If rains[i]>0, this means that lake rains[i] receives rain on day i, so we set ans[i]=−1 to indicate that no drainage is performed that day.
If rains[i] is raining for the first time, then there is no risk of flooding.
Otherwise, we must find the smallest index idx in st that is greater than the last day it rained on this lake. This can be implemented using binary search. If no such idx exists (i.e., there are no available sunny days for drainage), then a flood is unavoidable, and we should return an empty array as required by the problem. Otherwise, we set ans[idx]=rains[i] and remove idx from st, indicating that we will drain lake rains[i] on day idx to prevent flooding on day i.

---

### 🧪 Complexity

- **Time:** O(n log(n))
- **Space:** O(n)