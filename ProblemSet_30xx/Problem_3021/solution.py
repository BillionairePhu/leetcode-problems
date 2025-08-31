# Write your solution here
class Solution:
  def flowerGame(self, n: int, m: int) -> int:
    xeven = n//2
    xodd = n - xeven
    yeven = m//2
    yodd = m - yeven
    return xeven * yodd + xodd * yeven