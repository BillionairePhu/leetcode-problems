class Solution:
  def runningSum(self, nums: List[int]) -> List[int]:
    prefixes = [nums[0]]
    for i in range(1,len(nums)):
      prefixes.append(prefixes[-1]+nums[i])
    return prefixes