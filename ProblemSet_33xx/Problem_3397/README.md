# 🔥 Leetcode Problem (3397)

> **Problem:** [Maximum Number of Distinct Elements After Operations](https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Greedy`, `Sorting`

---

### ✅ Intuition

This is a very typical and interesting Greedy problem.

We can notice that each number has a range of values that they can mutate into, and we need to pick the mutated values such that it maximizes the total count of distinct values. As a result, we must pick in some way that minimize duplication.

The trick is to sort the array and start either top down or bottom up. After sorted, let's say we are going bottom-up, we need to prioritize picking the smallest possible unique value first, so that each time we pick a unique value, the picking range decreases - the lower bound goes up (imagine a bottle of water getting filled over time) and when we move to larger element, we move the bound upwards.

---

### 🧪 Complexity

The complexity here is mostly for sorting.

- **Time:** O(n log n)
- **Space:** O(n)