# 🔥 Leetcode Problem (3190)

> **Problem:** [Find Minimum Operations to Make All Elements Divisible by Three](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`, `Math`

---

### ✅ Intuition

If a number is divisble by 3, no operations are needed to turn it into multiple of 3. Else, we will need exactly 1 operation to turn it into multiple of 3 (add/minus 1 depending on the modulo of it by 3)

---

### 💡Implementation

Iterate through the array `nums` and count the number of elements not divisible by 3.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)