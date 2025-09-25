# 🔥 Leetcode Problem (2353)

> **Problem:** [Design a Food Rating System](https://leetcode.com/problems/design-a-food-rating-system/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Hash Table`, `String`, `Design`, `Heap (Priority Queue)`, `Ordered Set`

---

### ✅ Intuition

This is a very cool challenge to practice priority queue and hash table.

In order for us to quickly query the cuisine group and rating of a dish, we will use a hash table with the key being the name of the dish and the value being a list consisting of rating and cuisine group. 

Next, we can clearly see that this problem only cares about the dishes that have the highest ratings in its cuisine group. It leads to two ideas:

- We will have another hash table with each key links to a group (and dishes in that group).

- We will use a priority queue to store the dishes with its rating in each group for optimizing querying. But how about update? Do we need to find the dish, delete it and push new value in? Actually not! We can use soft delete - which means we only delete when we pop the heap and the value fetched is outdate (checking by comparing with the hash table of foods)
