# 2410. Booking Concert Tickets in Groups

Tag: `Binary Search`, `Segment Tree`

Link: [2410. Booking Concert Tickets in Groups](https://leetcode.com/problems/booking-concert-tickets-in-groups/description/)

## Intuition

There are 2 things we need to consider when doing this challenge:

- What data we need to store
- What functionalities we need to perform

### What data we need to store

Since there is a functionality `gather` that wants a number of consecutive seats in a certain row, so consecutive seats available in each row must be important.

However, it is also mentioned that the customers will always get the leftmost seats of a row. As a result, we only need to manage the number of seats available (no need to care about their positions - empty seats are always on the right).

=> A list of the number of empty seats in each row should be what we need to manage.

BUT in **what structure**? To answer that, let's look at the *functionalities*.

### What functionalities we need to perform

There are 2 functionalities:

- `gather`: determine if there are `k` consecutive empty seats in a row such that the row does not exceed `maxRow`. If there are, allocate `k` seats for the customers.

- `scatter`: determine if there are `k` empty seats (any empty seats) in rows which do not exceed `maxRow`. If there are, allocate `k` seats for the customers.

### Which data structure to use

It's observed that there are **a lot of query and update operations** when doing these functionalities. (query = getting number of seats for some rows; update = allocating seats)

As a result, using a traditional array would be too slow. Although updating is `O(1)`, calculating the sum/max number of seats in severals would have a complexity of `O(n)`.

Another option is to use prefix sum as query operation only takes `O(1)`, however, that would cause updating operation to have a complexity of `O(n)`.

A better solution is using **Segment Tree**, with the update operation having `O(log(n))` and the query operation of `O(log(n))`

=> We will store the data in a segment tree

## Implementation

Build a segment tree with each node storing the maximum seats in a row and the total number of seats for each segment.

Build `queryMax` to help `gather` function, the `queryMax` should prioritize the left node (only try the right node if leftnode cannot satisfy) and return `[]` or `[{smallest_row_satisfied}, {first_seat_allocated}]`

Buid `querySum` to help `scatter`, this operation is typical for a segment tree.

For `scatter`, since we might need to update many rows, we should have a variable to mark the last row that is full (so we can try to allocate from the next row - not repeating from the beginning)
