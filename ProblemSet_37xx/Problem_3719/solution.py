from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            oddCount, evenCount, numSet = 0, 0, set()
            for j in range(i, len(nums)):
                if (nums[j] not in numSet):
                    if (nums[j] % 2 == 0):
                        evenCount += 1
                    else:
                        oddCount += 1
                    numSet.add(nums[j])
                if (evenCount == oddCount):
                    # print(numSet)
                    result = max(result, j-i+1)
        return result

s = Solution()
print(s.longestBalanced([2,5,4,3]))
print(s.longestBalanced([1,2,3,2]))