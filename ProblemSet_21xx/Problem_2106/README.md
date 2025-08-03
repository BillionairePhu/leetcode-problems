# 🔥 Leetcode Problem (2106)

> **Problem:** [Maximum Fruits Harvested After at Most K Steps](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Array`, `Binary Search`, `Sliding Window`, `Prefix Sum`

---

### ✅ Intuition

The indices that one could travel from `startPos` would be in the range [`startPos - k`, `startPos + k`].

The idea here is that we would go from `startPos` toward index `i` in the range mentioned above and after hitting `i`, turn around and go in the other direction with the remaining steps.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)