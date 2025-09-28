from typing import List


class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    nums.sort()
    for i in range(2,len(nums))[::-1]:
      if (nums[i-1] + nums[i-2] > nums[i]):
        return nums[i-1] + nums[i-2] + nums[i]
    return 0