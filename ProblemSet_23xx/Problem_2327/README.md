# 🔥 Leetcode Problem (2327)

> **Problem:** [Number of People Aware of a Secret](https://leetcode.com/problems/number-of-people-aware-of-a-secret/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Dynamic Programming`, `Queue`, `Simulation`

---

### ✅ Intuition

This is a very good problem to practice queue.

We need to keep track of the number of people discovering the news by each day because the day they discover affects when they forget and when they spread the news. Since the day are linear and we don't need to keep track of those who forgot the news, we can simply use a queue with the size of the `forget` days.

We will iterate day by day and pop left of the queue (simulating people forgetting) and append new `spread` to the queue (people who just discover the news that day).

We will stop at the `n` day and calculate the total number of people remembering the news.

---

### 🧪 Complexity

Let `n` be the number of days this problem is asking us to query at. Let `f` be the number of days after which a person forget the news.

- **Time:** O(n)
- **Space:** O(f)