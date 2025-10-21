# 🔥 Leetcode Problem (3346)

> **Problem:** [Maximum Frequency of an Element After Performing Operations I](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Binary Search`, `Sliding Window`, `Sorting`, `Prefix Sum`

---

### ✅ Intuition

This is a very intriguing problem that asks you to implement multiple techniques to solve it.

First, we imagine that each value in the given array will have a range of values, which they can transform into. But each transformation will cost 1 operation and we can only perform a limited number of operation.

So the idea here is to find a value `x` that after using all operations wisely on the array, we obtain that most appearances of `x`. Note that `x` doesn't have to be a value in the given array.

We can start by counting the frequencies of each value. Why? Because it is more efficient to process based on the frequency rather than the array itself. For example, we do not need to process an array of 4 number `5` - [5,5,5,5] but rather as: the number (key) `5` has a frequency of 4.

Then, we sort the keys in ascending order so that we can process iteratively and more importantly, we can compute the prefix sum of the frequency array!! The frequency array will help as the frequency in a range quickly O(1)!!!

Finally, we iterate from the first key to the last key - let's say the currently processed key is `n` - and calculate the frequency of the ranges:

- [`n-k`, `n+k`] => after operations become `n`
- [`n-2*k`, `n`] => after operations become `n-k`

Why these 2 ranges? The first range is quite intuitive, since the frequency at `n` itself doesn't any operations, transforming other numbers to it would maximize the frequency. Now, the second range is less intuitive but it is important to calculate the frequency of it because given a sufficient number of operations, we can transform as many numbers to an intermediate number, which should be in the middle of the range.

---

### 🧪 Complexity

- **Time:** O(n log n)
- **Space:** O(n)