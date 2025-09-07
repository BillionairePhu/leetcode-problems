from typing import List


class Solution:
  def sumZero(self, n: int) -> List[int]:
    result = []
    mod_n = n % 2
    div_n = n // 2
    for i in range(div_n):
      result.append(-1 * (i+1))
      result.append(1 * (i+1))
    if (mod_n == 1):
      result.append(0)
    return result