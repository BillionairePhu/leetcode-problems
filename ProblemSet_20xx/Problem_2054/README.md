# 🔥 Leetcode Problem (2054)

> **Problem:** [Two Best Non-Overlapping Events](https://leetcode.com/problems/two-best-non-overlapping-events/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Binary Search`, `Dynamic Programming`, `Sorting`, `Heap (Priority Queue)`

---

### ✅ Intuition

The problem asks us to choose 2 events such that there is no overlapping time between them. In other words, the latter event must begin strictly after the first event.

From this description, we can infer that we need to sort the events either by its `beginTime` or `endTime` so that when processing, we can just iteratively process the events without worrying about the unordered time. For this problem, let's stick with sorting the events by `endTime`.

For each event `i`, we must find another event `j` ending before the starting time of event `i` such that the value of `j` is maximum. Naively, we can have a nested loop for every possible `j` ending before `i` to do this, but the algorithm will take O(n^2) and exceeds the time limit.

To optimize this, we can implement dynamic programming + binary search. We can dynamically compute the maximum value of events up until time `i` and store in a `dp_values` array. While doing that, we also adds that time `i` to the `time_frames` array - this will help us binary search when needed. For each `i`, we will update the `dp_values` array (max of the previous `dp_values[i-1]` and the current event's value) and `time_frames` array. The `result` will also be updated by getting max of the current `result` and the value when combining the current event with the most-valued event ending before it (by binary-search the `time_frames` and use that index to query `dp_values`).

---

### 🧪 Complexity

Let N be the number of events

- **Time:** O(N log N)
- **Space:** O(N)