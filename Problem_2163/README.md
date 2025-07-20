# 2163. Minimum Difference in Sums After Removal of Elements

Tag: `Array`, `Dynamic Programming`, `Heap`

Link: [Problem 2163. Minimum Difference in Sums After Removal of Elements](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/description/?envType=daily-question&envId=2025-07-18)

*I need to peak the Editorial to get some ideas :D turn out not hat hard*

## Intuitive

We would like to divide the array into 3 parts: the removed part, the left part (first n elements after removing) and the right part (last n elements after removing).

AND we want the difference between the left part and the right part to be smallest. => minimize left part and maximize right part.

We notice that the left part always has elementss of index smaller than `2*n` and the right part always has elements of index larger or equal to `n`.

Let `j` be some index that divides the array into two parts, on the left side (including `j`) is the left part and on the right side is the right part. `j` can only in the range `[n, 2*n-1]`. In addition, for each `j`, the left part will consist of `n` smallest numbers from `j` (including `j`) to the front; vice versa, for each `j` the right part will consist of `n` largest numbers from `j` (not including `j`) to the back.

Then, we can iterate `j` and calculate the minimum difference for each case of `j`. The result will be the minimum of those values.

## Approach

Use two heaps: one max heap for the left part and one min heap for the right part.

For the left part, we want to eliminate the largest value in the heap (to minimize the left part); for the right part, we want to eliminate the smallest value