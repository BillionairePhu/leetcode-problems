# 🔥 Leetcode Problem (3186)

> **Problem:** [Maximum Total Damage With Spell Casting](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `Two Pointers`, `Binary Search`, `Dynamic Programming`, `Sorting`, `Counting`

---

### ✅ Intuition

1. We will count the frequency of each number's appearance => this will decide how many points (damages) we can earn from choosing that number.

2. Sort the numbers (the keys) ascendingly.

3. Then we will start processing from the largest number backward to the smallest number. Here, we calculate the maximum points obtained from a scenario where we pick a number `n` and some other numbers that are larger than `n`. => Calculate this back to the smallest number and the result would be the maximum of all points we have calculated.

Ok. Now, the only problem is to how to calculate max points obtained from picking a number `n`. The key here is if we pick `n`, we cannot pick `n+1` or `n+2` so the next larger number we can pick must be `>= n+3` => The maximum point obtained is the points of picking `n` (calculated from the counter in step 1) plus the largest points from picking a number that is `>= n+3`.

---

### 🧪 Complexity

- **Time:** O(n * log n)
- **Space:** O(n)