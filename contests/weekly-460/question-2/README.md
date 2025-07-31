# 🔥 Problem (Weekly 460)

> **Problem:** [Maximum Number of Subsequences After One Inserting](https://leetcode.com/contest/weekly-contest-460/problems/maximum-number-of-subsequences-after-one-inserting/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Prefix sum`, `Math`

---

### ✅ Intuition

#### Solve the simplified problem

Let's consider the simplified problem: given the array `s`, what is the number of `LCT` subsequences (without inserting anything)?

- For each `T`, the number of `LCT` sequence ending with that `T` is the number of subsequences `LC` ending before that letter.

- To answer how many `LC` subsequence ending with a specific letter `C`, we need to find out how many `L` before that letter.

Combined, we can iterate from the first character to the last in the string and keep track of how many `L`, `LC`, `LCT` subsequences ending before or at each index.

The number of `L` increments by one each time we encounter an `L`; the number of `LC` increments by the number of `L` before the current index each time we encounter a `C`; the number of `LCT` increments by the number of `LC` before the current index each time we encounter a `T`.

#### Solve the full problem

There are 4 cases we can consider when inserting a letter to the array:

- The letter is not `L`, `C` or `T`: the number of `LCT` subsequences stay the same as not inserting the letter.

- The letter is a `L`: we would want to insert it at the very beginning of the array to maximize the number of `LCT` subsequences

- The letter is a `T`: we would want to insert it at the very end of the array to maximize the number of `LCT` subsequences

- The letter is a `C`: when inserting `C` at a certain index, it would increase the number of `LCT` subsequences by ("the number of `L` before it" multiply by "the number of `T` after it"). For this case, we need to consider all possibles `C` index

---

### 💡Implementation

Divide into three cases as mentioned above and calculate the number of `LCT` subsequences for each case.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)