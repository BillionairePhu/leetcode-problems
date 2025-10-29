from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        result, prefix = 0, [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        for i in range(len(nums)):
            if (nums[i] != 0):
                continue
            
            left, right = prefix[i], prefix[-1] - prefix[i+1]
            if (left == right or left == right+1):
                result += 1
                
            if (right == left or right == left+1):
                result += 1
        return result
    
s = Solution()
print("Result", s.countValidSelections([1,0,2,0,3]))