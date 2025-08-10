# 🔥 Leetcode Problem (3363)

> **Problem:** [Find the Maximum Number of Fruits Collected](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Array`, `Dynamic Programming`, `Matrix`

---

### ✅ Intuition

Although labeled as a Hard problem, this is indeed very easy. You just need to realize that the path for 3 kids are in fact not crossed, each of them has a separate area they can walk.

> This happens because each kid can only take n-1 steps, they only have just enough step to reach the destination - not extra to wander around.

The first kid has one single path to walk (1,1) -> (2,2) -> ... -> (n-1,n-1)

The second and third kid cannot cross the first kid's path.

Therefore, we just straightforward calculate the maximum candies each kid can collect and take the sum of them.

---

### 🧪 Complexity

- **Time:** O(n^2)
- **Space:** O(1)