from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        first_seq, second_seq, i = 1, 1, 1
        
        while (first_seq < k or second_seq < k) and i < len(nums) - k:
            if (nums[i] <= nums[i-1]):
                first_seq = 1
            else:
                first_seq += 1
                
            if (nums[i+k] <= nums[i+k-1]):
                second_seq = 1
            else:
                second_seq += 1
            i += 1
        return (first_seq >= k and second_seq >= k)

s = Solution()
print(s.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3))
print(s.hasIncreasingSubarrays([-15, 19], 1))