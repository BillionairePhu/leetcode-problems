# 1900. The Earliest and Latest Rounds Where Players Compete

Tag: `Dynamic Programming`, `Memoization`

Link: [Problem 1900 - The Earliest and Latest Rounds Where Players Compete](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/description/?envType=daily-question&envId=2025-07-12)

## Intuitive

`The relative order of all the meetings should stay the same and they should remain non-overlapping.`

This problem is actually simple, when shifting 1 meeting to maximize the continuous freetime, it's actually finding the 2 consecutive freetime slots that combines being the largest freetime (by shifting the meeting between them to the leftmost or rightmost)

## Approach

Convert the given data to an array of freetimes. Then iterate through those freetimes to find **k+1** consecutive freetimes that combines the largest.

**Follow up problem**:

- [Problem 3440 - Reschedule Meetings for Maximum Free Time II](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/description/?envType=daily-question&envId=2025-07-10)