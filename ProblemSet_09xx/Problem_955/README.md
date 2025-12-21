# 🔥 Leetcode Problem (955)

> **Problem:** [Delete Columns to Make Sorted II](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `String`, `Greedy`

---

### ✅ Intuition

Let's sum up the problem's requirement: it wants us to delete the minimum number of columns such that the resulting strings are in lexicographically order.

In other words, for any two valid consecutive strings in the array, the latter must be lexicographically larger than the previous one. And lexicographically, the left-er columns will have higher priority so we need to check from left to right.

We will  have an `equal_prev` array to keep track if the `i`-th string is equal to its previous string => There is a chance that when appending a suffix to it, the order is not kept.

Ok, now we will check if the column `col_index` needs deletion by going through each string in the `strings` array and focus on the `col_index` character. But first if the current string is already strictly larger than the previous string (indicated by `equal_prev` array), we don't can skip to the next string. Otherwise, we compare the `col_index` character of the current string with that of the previous one. If it violates the order, we need to delete it. And if we don't need to delete it, we need to update if a string is no longer equal to the previous string.

---

### 🧪 Complexity

- **Time:** O(M*N)
- **Space:** O(M)