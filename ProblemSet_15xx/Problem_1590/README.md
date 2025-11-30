# 🔥 Leetcode Problem (1590)

> **Problem:** [Make Sum Divisible by P](https://leetcode.com/problems/make-sum-divisible-by-p/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Prefix Sum`

---

### ✅ Intuition

The main aim that we are trying to solve here is finding a subarray such that when removing it from the given array, the remaining elements' sum is divisble by `p`.

The take-away key here is that the removed array's sum will have a modulo (by `p`) of `k` and so does the given array's sum. The reason is very simple: the remaining elemnts' sum has a modulo of 0 (divisible by `p`).

OK, now consider how can we calculate the modulo of any given subarray? We can do that easily by iterating through each element and calculating the prefix sum ending at that location (plus the modulo of it).

=> To find the modulo of a subarray (beginning from `a` and ending at `b`), we take the modulo of the prefix at `b` minus the modulo of the prefix sum at `a-1`. Simple!!

But actually, we don't need to calculate modulo of all subarrays. We only need to care about what the shortest array with a modulo of `k` is. Thus, we only need to keep track of the latest index, which each modulo presents, is.

---

### 🧪 Complexity

Let the length of the given array be `n`.

- **Time:** O(n)
- **Space:** O(n)