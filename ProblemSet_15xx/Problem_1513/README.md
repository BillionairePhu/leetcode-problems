# 🔥 Leetcode Problem (1513)

> **Problem:** [Number of Substrings With Only 1s](https://leetcode.com/problems/number-of-substrings-with-only-1s/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Math`, `String`

---

### ✅ Intuition

Quite simple, we just need to iterate from the first character to the last one and count the `all-1`-substring that ends with it.

---

### 💡Implementation

Keep track of the number consecutive one ending at each number, the number of `all-1` substring will be that count.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)