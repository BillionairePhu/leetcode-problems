from typing import List


class Solution:
  def gcd(self, a: int|None, b: int|None) -> int:
    if (a == None or b == None):
      return 1
    while b != 0:
        a, b = b, a % b
    return a
  
  def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
    result = []
    prev = None
    for num in nums:
      gcd_nums = self.gcd(prev, num)
      if (gcd_nums > 1):
        prev = gcd_nums * (prev // gcd_nums) * (num // gcd_nums)
      elif (prev == None):
        prev = num
      else:
        self.mergeToResult(result, prev)
        prev = num
    self.mergeToResult(result, prev)
    return result
  
  def mergeToResult(self, result: list[int], num: int):
    while len(result) > 0:
      last_num = result[-1]
      n = self.gcd(num, last_num)
      if (n > 1):
        result.pop()
        num = n * (num // n) * (last_num // n)
      else:
        break
    result.append(num)
  
s = Solution()
print(s.gcd(899, 23))
# print(s.replaceNonCoprimes([6,4,3,2,7,6,2]))
print(s.replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825]))