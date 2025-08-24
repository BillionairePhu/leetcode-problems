from typing import Counter, List


class Solution:
  def partitionArray(self, nums: List[int], k: int) -> bool:
    if (len(nums) % k != 0):
      return False
    numGroups = len(nums) // k
    counter = Counter()
    for num in nums:
      counter[num] += 1
      if (counter[num] > numGroups):
        return False
    return True
  
s = Solution()
print(s.partitionArray([1,2,3,4],2))