from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        pos = [-1] * 31
        results = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(pos)):
                if (nums[i] & (1 << j) != 0):
                    pos[j] = i
            max_pos = max(pos)
            results[i] = max_pos - i + 1 if (max_pos > -1) else 1
        return results
            
s = Solution()
print("Result", s.smallestSubarrays([1,0,2,1,3]))