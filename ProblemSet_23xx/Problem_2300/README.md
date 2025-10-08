# 🔥 Leetcode Problem (2300)

> **Problem:** [Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Two Pointers`, `Binary Search`, `Sorting`

---

### ✅ Intuition

Sort the potions ascendingly and now that we have a list sorted, we can use binary search to quickly find the index, from which all potions will create successful pair with the current spell.

---

### 🧪 Complexity

Let n be number of spells and m be the number of potions.

- **Time:** $O(n*log(m) + m*log(m))$
- **Space:** $O(m + n)$