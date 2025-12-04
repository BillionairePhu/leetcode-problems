# 🔥 Leetcode Problem (2211)

> **Problem:** [Count Collisions on a Road](https://leetcode.com/problems/count-collisions-on-a-road/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `String`, `Stack`, `Simulation`

---

### ✅ Intuition

From the problem description, we can realize that each car can contribute maximum one to the result and the contribution happens if and only if that car is moving and there is a colission involving that car.

That basically leads us to our approach, we can iterate each vehicle from left to right, and for direction of it, we can divide into these processing branch:

- If the vehicle is moving to the left, a collision only happens if there exists obstacle on the left (which are staying cars or cars moving to the right). Note that another car to the left of it moving left does not constitute an obstacle because they travel at the same speed.

- If the vehicle is staying, then it will not contribute to the collision count. But it could be an obstacle.

- If the vehicle is moving to the right, it will contribute one to the collision if there is an obstacle to the right of it (vehicle moving left or staying vehicle). But since we are iterating from the left to right, we can increment a variable for storing the number of cars moving to the right and "cash out" when we meet an obstacle to the right of it.

---

### 💡Implementation

Ok, based on the logic above, we can have a simple for loop with 3 branches to process that.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)