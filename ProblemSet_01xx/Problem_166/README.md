# 🔥 Leetcode Problem (166)

> **Problem:** [Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Hash Table`, `Math`, `String`

---

### ✅ Intuition

Wow, I have been using the calculator my whole life and taken for granted that the computer instantly knows at which point the digits starting to repeat. This problem is really interesting and makes me think for a while.

The idea here is actually very simple, we divides the numerator by the denominator and if cannot, we multiply that numerator by 10 to get a new numerator and repeats the process (just like how we calculate division in elementary school). The important question is: when does the digit starts to repeat!!! => We keep track of all the numerators we have processed, if at a time, we see any of the processed number then we have reach a loop.

---

### 💡Implementation

Use hashed set to store a list of processed numerators and add new number to that list every time we process (dividing the numerator by denominator and then multiply by 10).

---

### 🧪 Complexity

I don't think there is a way to know the complexity of it given the numerator `n` and denominator `m` since the complexity would linearly scale with the length of the repeating sequence of the result. However~~ to know the repeating length, we need to solve for the number `S` such that `S = 9999999999999...999` (repeating 9) and `S` is divisible by `m` => This is a factor problem and NP hard.

- **Time:** O(?)
- **Space:** O(?)