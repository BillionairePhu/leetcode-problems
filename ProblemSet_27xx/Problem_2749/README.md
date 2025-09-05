# 🔥 Leetcode Problem (2749)

> **Problem:** [Minimum Operations to Make the Integer Zero](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Bit Manipulation`, `Brainteaser`, `Enumeration`

---

A very tricky question, I think this should be rated as Hard since you need to notice the effect of the problem constraints. I had to see all the hints to solve, especially the 3rd and 4th hint.

---

### ✅ Intuition

The most important point you need to realize when doing this problem is that "if it is possible to make `num1` equal to 0, then we need at most 60 operations"!!!

Why is that?!? It is because the constraint of the problem forced it to be - I will explain why later.

#### Simple sub-problem

First, let's do a subproblem - this problem without `num2` (a.k.a `num2` = 0). Then, the problem is actually counting the number of `1`s in the binary representation of `num1` - cause every operation will remove 1 single instance of `one` in its representation. *Very simple, I believe there is another medium problem exactly like this.*

#### Solve the main problem

Now, get back to case where `num2` is not 0. For every operation you do, `num1` will substract `num2` one time. As a result, if the correct result is `n` operations then it is possible to subtract `k = num1 - n * num2` `n` times with some power of 2 to be equal to 0. How can we know if it is possible or not? Very simple, let's look back to the subproblem above, the minimum number operations needed must be at least the number of `ones` in the binary presentation of `k`. Also the number of operations must be at maximum `k` (duh, because one operation takes away at least 1 - which is `2^0`).

Ohhh, we can just iterate through the number of operations and check if it is the correct answer. :oooo Wait~~ We iterate from 1 operation, but when do we stop? There exists cases that we can never make `num1` become 0 using the given operation (one example is test case 2 of this Leetcode problem). The answer is 60!!!

#### Why iterating 60 operations is enough?

Because $-10^9 <= num2 <= 10^9$ and `i` is in the range [0, 60] :v I'm lazy so I will leave this as a challenge for you to figure out.

---

### 💡Implementation

You can implement as the `Intuition` above. The implementation is very simple.

---

### 🧪 Complexity

- **Time:** O(1)
- **Space:** O(1)