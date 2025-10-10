# 🔥 Leetcode Problem (3147)

> **Problem:** [Taking Maximum Energy From the Mystic Dungeon](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Prefix Sum`

---

### ✅ Intuition

Since we are jumping `k` steps every time, the magicians can be divided into `k` groups by assigning the magician at index `i` to `i % k`-th group.

As a result, each option of the problem only involves magicians in one group only. Thus, we can calculate the highest energy obtained regarding each group.

In general, the maximum energy you can get at index `j` is either the maximum energy you can get at index `j - k` plus the energy at index `j` or the energy at index `j` itself. Following this idea, we can iterate from 0 to the final numbers to get the maximum energy at the final indices of each group. 

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(k)