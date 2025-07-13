# 2410. Maximum Matching of Players With Trainers

Tag: `Sorting`, `Greedy algorithm`

Link: [Problem 2410 - Maximum Matching of Players With Trainers](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/?envType=daily-question&envId=2025-07-13)

## Intuitive

First, sort the arrays of players and trainers.

Then go from left to right, try to match first player with first trainer

- If cannot, keep the player but move to the next trainer
- If can, move to the next player and move to the next trainer