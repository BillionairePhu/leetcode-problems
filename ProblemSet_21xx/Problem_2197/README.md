# 🔥 Leetcode Problem (2197)

> **Problem:** [Replace Non-Coprime Numbers in Array](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Array`, `Math`, `Stack`, `Number Theory`

---

### ✅ Intuition

To check if two numbers are co-prime, we can use the Euclidean algorithm. This algorithm finds the GCD (greatest common divisor) of 2 numbers => if GCD of 2 numbers equal 1 then they are co-prime.

To merge the non-coprime numbers, we can traverse from index 0 to the end and use stack to keep in mind the possibility to merge the previous element in the stack.

---

### 🧪 Complexity

Let `n` be the length of the array and `r` be the largest value of an integer in that array.

We have to iterate through each number in the array, which is `n` steps and for each step we need to calculate the Euclidean algorithm, which has the time complexity of O(log(r)).

- **Time:** O(n * log(r))
- **Space:** O(n)