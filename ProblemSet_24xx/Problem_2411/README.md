# 🔥 Leetcode Problem (2411)

> **Problem:** [Smallest Subarrays With Maximum Bitwise OR](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Binary Search`, `Bit Manipulation`, `Sliding Window`

---

### ✅ Intuition

For each number, we process for each bit: what is the nearest number (after our current number) which has that bit being 1? *Note: there could exist no such number*. Then the minimum-sized array with maximum value would need to extend to at least that number.

To reuse our calculation of, we will solve the problem from the last number back to the first number.

---

### 💡Implementation

Since the maximum number of bits possible for this problem is 30 (10 ^ 9), we initialize an array of at least 30 elements to store the closest position which has that bit being 1.

Initialize the array with the values -1 (no position satisfied)

```python
pos = [-1] * 31
```

Then we iterate from the back to the front, for each number we iterate through, we updates the `pos` array. If the current number has the `i`-th bit being one, update `pos[i]` to be the current number index.

Then the minimum-sized array starting from the current index would be from itself to the largest of all positions in `pos`. If there are no appearance in `pos`, the minimum-sized array should be itself (length = 1)

```py
max_pos = max(pos)
results = max_pos - i + 1 if (max_pos > -1) else 1
```

---

### 🧪 Complexity

- **Time:** O(n * k)

`n` is the number of elements in the input array.

`k` is the number of bits of that the largest number for this problem might have (in this case 30 because the max number is 10^9)

The time complexity is `O(n*k)` because we need to iterate one time for each of `n` elements in the array (from the back to the front) and for each iteration, we need to process every possible bits (`k`).

- **Space:** O(n)