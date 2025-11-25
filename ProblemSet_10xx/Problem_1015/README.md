# 🔥 Leetcode Problem (1015)

> **Problem:** [Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Hash Table`, `Math`

---

### ✅ Intuition

Assume that we have a number A = 1...1 (*`n` repeating number 1*) then $\overline{A1} \equiv 10*A + 1 (\mod k)$.

Using the above property, we can try to increase the length of `A` until we find a number that is divisble by `k`.

But when do we stop? What if there is no such number, will we increment until infinity? Yes, this is a problem that we need to consider. The answer is very simple, the changing of modulo when incrementing is a cycle so we will stop when we hit the same modulo again. (Imagine if the current modulo is `x` then the next modulo is ALWAYS `10*x + 1`). Cool, then we only need to increment at most `k` times - because there can only be `k` modulo values

---

### 💡Implementation

Make a loop to get the modulo of the next number and check if it is divisble by `k`. We only need to keep track of the modulo value, not the number itself.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(n)