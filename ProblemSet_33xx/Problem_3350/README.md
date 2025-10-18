# 🔥 Leetcode Problem (3350)

> **Problem:** [Adjacent Increasing Subarrays Detection II](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Binary Search`

---

### ✅ Intuition

The problem ask us to find maximum k such that there exist nums[i:i+k] and nums[i+k:i+2k] are strictly ascending. This is very similar to the other problem `Adjacent Increasing Subarrays Detection II` (3349).

We just need to iterate `i` from index 0 to the end and while doing that, count the max-length `seqs[i]` of ascending sequences ending at index `i`. 

- Then we can calculate max `k` so far (up to `i`) by updating `k` equal `seqs[i]` if `seqs[i-k]` is larger than or eqqual to `seqs[i]`. Why? Here, we are actually considering if `k` can be `seqs[i]` and the second (latter) sequence is ending at index `i`.

- Also, if not, we need to update `k` equal `seqs[i]//2` if `seqs[i] // 2` is larger than `k`. It is because, we can always split the current ascending seqquence into 2 consecutive ascending sequences.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)