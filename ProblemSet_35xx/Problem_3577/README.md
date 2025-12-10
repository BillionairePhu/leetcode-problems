# 🔥 Leetcode Problem (3577)

> **Problem:** [Count the Number of Computer Unlocking Permutations](https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Math`, `Brainteaser`, `Combinatorics`

---

### ✅ Intuition

Haha, this is actually a trick question. At first, I was thinking that this might be a backtracking, dynamic programming problem.

But the key here is to realize that if the number of password that you can unlock at any given time is the same (of course minus the one already unlocked) because there is no way to expand/discover more password. This is primarily due to the problem's condition (To decrypt the password for computer i, you must have already unlocked a computer j such that j < i and complexity[j] < complexity[i].)

So basically, it only asks you to check if all `complexity[i]` (i>0) are greater than `complexity[0]` and calculate `(n-1)!`

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)