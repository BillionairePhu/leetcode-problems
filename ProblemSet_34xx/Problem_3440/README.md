# 3440. Reschedule Meetings for Maximum Free Time II

Tag: `Greedy`, `Array`, `Enumeration`

Link: [Problem 3440](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/description/?envType=daily-question&envId=2025-07-10)

## Intuitive

This problem is similar to problem **3439** however it allows for changing the relative position of the meetings. So the maximum freetime is in fact the maximum sum of the 2 consecutive freetimes (plus the duration of the meeting in-between if there is another freetime somewhere to move that meeting to)

## Approach

- Convert the given data to an array of freetimes and meeting durations.

- Keep track of the 3 biggest freetimes so that we can move the in-between meeting to.

- Iterate through the freetime and find the combination time of each pair of consecutive freetimes (plus the duration of in-between meeting if it's movable)

**Follow up problem**:

- [Problem 3439 - Reschedule Meetings for Maximum Free Time I](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/?envType=daily-question&envId=2025-07-09)