# 🔥 Leetcode Problem (3349)

> **Problem:** [Adjacent Increasing Subarrays Detection I](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`

---

### ✅ Intuition

We can calculate the length of the ascending sequence ending at index `i` by iterating from index 0 to `i` and incrementing a `count` variable every time the current number at `i` is larger than the one at `i-1`. Remember to reset the `count` to 1 if it's not ascending (why 1 and not 0? because one number could be an ascending sequence of length 1).

OK =D so we have managed to calculate the length of ascending sequence at index `i`. Now the problem only ask us to check if there exists two ascending sequence at index `j` and `j+k` and they both have length = k. Sound simple, right?

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)