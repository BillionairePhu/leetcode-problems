# 🧠 Leetcode Problem 1717

This problem asks you to try maximizing the score obtained by performing operations on a string. There are operation type that you can perform:
- Remove substring "ab" and gain `x` points.
- Remove substring "ba" and gain `y` points.


## ✅ Solution Strategy

From logical thinking, we realize that this problem can be solved by greedily remove the substring that gives us the higher points first and then remove the other substring. You can think about this and see that this greedy way will always give the best result.

However, when removing a substring, a new substring could appear, which might be removable; as a result, we need to try to remove again until we cannot remove anything left.

## 🔗 Leetcode Link

[https://leetcode.com/problems/{problem_number}](https://leetcode.com/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2025-07-23)