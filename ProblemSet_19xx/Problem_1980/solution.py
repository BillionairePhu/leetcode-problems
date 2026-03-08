from typing import List


class Solution:
  def findDifferentBinaryString(self, nums: List[str]) -> str:
    n = len(nums[0])
    num_set = set()
    
    for num in nums:
      num_set.add(int(num,2))
      
    for i in range(2 ** n):
      if (i not in num_set):
        return bin(i)[2:].zfill(n)
    return -1
    
s = Solution()
print("Result", s.findDifferentBinaryString(["01","10"]))
print("Result", s.findDifferentBinaryString(["00","01"]))
print("Result", s.findDifferentBinaryString(["111","011","001"]))
