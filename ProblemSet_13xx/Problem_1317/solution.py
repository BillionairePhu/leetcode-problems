from typing import List


class Solution:
  def getNoZeroIntegers(self, n: int) -> List[int]:
    def isNoZero(n: int) -> bool:
      return '0' not in str(n)
    
    for i in range(1 + (n+1) // 2):
      if (isNoZero(i) and isNoZero(n-i)):
        return [i, n-i]
      
s = Solution()
print(s.getNoZeroIntegers(2))
print(s.getNoZeroIntegers(10))