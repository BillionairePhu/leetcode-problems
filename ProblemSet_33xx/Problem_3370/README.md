# 🔥 Leetcode Problem (3370)

> **Problem:** [Smallest Number With All Set Bits](https://leetcode.com/problems/smallest-number-with-all-set-bits/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Math`, `Bit Manipulation`

---

### ✅ Intuition

This is an easy bit manipulation problem. We just need to try all-set-bit numbers from the smallest one (which is `1`) up until we found a number greater than `n`.

---

### 💡Implementation

It can simply be done by having an iteration loop and adding a bit to the previous trial number (which can be broken down into two operations: shift-left and addition, e.g. adding a set bit to number one in binary format `1` -> `10` -> `11`)

---

### 🧪 Complexity

- **Time:** O(log n)
- **Space:** O(1)