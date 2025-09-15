# 🔥 Leetcode Problem (1935)

> **Problem:** [Maximum Number of Words You Can Type](https://leetcode.com/problems/maximum-number-of-words-you-can-type/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Hash Table`, `String`

---

### ✅ Intuition

Just iterate through the words (separated by whitespace) and check if there is any character in it that is in the broken words list (we can use set - hash table to optimize the check operation)

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)