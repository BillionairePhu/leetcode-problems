# 69. Sqrt(x)

Tag: `Binary Search`, `Mathematics`

Link: [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

## Intuition

This is an interesting problem that asks a very fundamental math problem. This square root problem has been investigated a very long time ago, at least 1000 BCE.

#### What is a square root?

A square root of a number `S` is `x` if `x^2 = S`. 

#### What property can we find?

The polynomial (`y = x^2`) is monotonic for `x > 0` so in the positive range, if `a^2 > S` then `a > x` and vice versa. This property is enough for us to derive a binary search for this problem.

## Approach

There are several approaches to this problem. I'm gonna do 2 of them.

#### Binary search

This is the itended approach of Leetcode. We will do binary search in the range of [0, S] until we find the largest x that `x^2 <= S` (because the problem asks us to floor down the result)

To do binary search, just divide the range of searching in the middle until we reach a point where there is only one number left. *(See the code)*

But remember the question ask us to floor down so we need to pick a number that when squared smaller or equal to x.

#### Code
```python3 []
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while (low < high):
            mid = (low + high) // 2
            if (mid * mid > x):
                high =  mid - 1
            else:
                low = mid + 1
            
        return low if low * low <= x else low - 1
```

#### Heron's method approach

Another approach using Mathematical property is Heron's method.

#### Code
```python3 []
class Solution:
    def mySqrt(self, x: int) -> int:
        iterations = 100
        result = 1
        # Increase iteration to increase accuracky
        for _ in range(iterations):
            result = 0.5 * (result + x/result)
        return int(result) # Get the floored integer of the result
```