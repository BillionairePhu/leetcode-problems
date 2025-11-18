# 🔥 Leetcode Problem (717)

> **Problem:** [1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Array`

---

### ✅ Intuition

Hah, interesting problem. This is a Huffman coding problem!

We just need to read from left to right and matching words whenever we saw a valid word. Then, we just need to keep track of the last word and checking if that last word is 1-bit.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)