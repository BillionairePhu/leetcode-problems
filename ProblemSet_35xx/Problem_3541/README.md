# 🔥 Leetcode Problem (3541)

> **Problem:** [Find Most Frequent Vowel and Consonant](https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/)<br />
> **Difficulty:** Easy<br/>
> **Tags:** `Hash Table`, `String`, `Counting`

---

### ✅ Intuition

Very simple just count the appearances of each vowel and consonant then find the maximum for vowel appearances and consonant appearances. Just like the challenge description.

---

### 💡Implementation

Use a hashed table to easily update and access the number of appearances of each letter. Iterate through the string's characters and increment the corresponding letter's appearance.

---

### 🧪 Complexity

- **Time:** O(n)
- **Space:** O(1)