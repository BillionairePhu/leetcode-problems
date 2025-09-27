from typing import List


class Solution:
  def triangleNumber(self, nums: List[int]) -> int:
    result = 0
    
    nums.sort()
    
    for i in range(len(nums)-2):
      index = len(nums) - 1
      for j in range(i + 1, len(nums)-1)[::-1]:
        if (nums[i] == 0):
          continue
        while index > j and nums[i] + nums[j] <= nums[index]:
          index -= 1
        result += (index - j)
        print(i, j, index)
    return result
  
s = Solution()
print("Result", s.triangleNumber([2,2,3,4]))
# print("Result", s.triangleNumber([0,0,0,0]))