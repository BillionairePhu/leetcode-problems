from math import floor, sqrt


class Solution:
  def countTriples(self, n: int) -> int:
    result = 0
    for a in range(1, n+1):
      for b in range(1, n+1):
        c = sqrt(a**2 + b**2)
        if (c % 1 != 0 or c > n):
          continue
        result += 1
    return result