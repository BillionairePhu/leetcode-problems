# 3201. The Earliest and Latest Rounds Where Players Compete

Tag: `Array`, `Parity`

Link: [Problem 3201 - Find the Maximum Length of Valid Subsequence I](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/?envType=daily-question&envId=2025-07-16)

## Intuition

The valid subsequence should have all consecutive pair of numbers having the same parity for their sums.

## Approach
    
There are 4 cases for longest valid subsequence, so the most simple way is just count the subsequence in those 4 case:

- Subsequence has the pair parity of even, starting with an even number
- Subsequence has the pair parity of even, starting with an odd number
- Subsequence has the pair parity of odd, starting with an even number
- Subsequence has the pair parity of odd, starting with an odd number
