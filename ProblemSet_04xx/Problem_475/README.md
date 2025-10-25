# 🔥 Leetcode Problem ({{ frontendQuestionId }})

> **Problem:** [Heaters](https://leetcode.com/problems/heaters/description/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Two Pointers`, `Sort`

---

### ✅ Intuition

We will sort the houses and heaters and then for each house, we will find the closest heater to the left and to the right of it. Since we have sorted before, this will be just an iteration problem.

---

### 🧪 Complexity

Since sorting has a greater complexity than linear iteration, the complexity of this problem will be based on the sorting complexity.

- **Time:** O(n log n)
- **Space:** O(n)