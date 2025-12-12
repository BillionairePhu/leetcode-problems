# 🔥 Leetcode Problem (3433)

> **Problem:** [Count Mentions Per User](https://leetcode.com/problems/count-mentions-per-user/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Math`, `Sorting`, `Simulation`

---

### ✅ Intuition

This problem basically asks you to count the mentions for each person. => keep track of the mentions for each person

For `ALL` mention, this is easy: just increment all mention by 1.

For specific `id<number>` mention, it is also easy: just increment the mention for that person only.

The real trouble is for `HERE` mention: we need to know which person is online at that time and increment only online people. The way to do this is to process the events in time order => sorting the event by timestamp (remember to put OFFLINE event before MESSAGE event!!!). Then you can iteratively update the next online time of each person, this "next_online" will be the condition for incrementing `HERE` mention.

---

### 🧪 Complexity

Let the number of event be `n` and the number of persons be `m`

- **Time:** O(n * log(n) * m)
- **Space:** O(n + m)