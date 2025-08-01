from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result = nums[0]
        
        left = 0
        sum = nums[0]
        myset = set([nums[0]])
        for i in range(1, len(nums)):
            while (nums[i] in myset and left < i):
                myset.remove(nums[left])
                sum -= nums[left]
                left += 1
            sum += nums[i]
            myset.add(nums[i])
            if (sum > result):
                result = sum
            # print(i, result, left)
        return result
    
s = Solution()
# print(s.maximumUniqueSubbarray([4,2,4,5,6]))
print(s.maximumUniqueSubbarray([5,2,1,2,5,2,1,2,5]))
            