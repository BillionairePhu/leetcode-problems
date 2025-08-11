# 🔥 Leetcode Problem (2438)

> **Problem:** [Range Product Queries of Powers](https://leetcode.com/problems/range-product-queries-of-powers/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Bit Manipulation`, `Prefix Sum`

---

### ✅ Intuition

Iterate through the powers of 2 to find out which numbers will add up to `n`. However, the trick here is to store only the power, not the whole number (e.g. 8 -> store 3 because 8 = 2^3). By doing this, we can keep the storing number small.

To get the multiplication of the query, we generate a prefix sum of the stored powers => each query only needs to calculate the power of the result

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)