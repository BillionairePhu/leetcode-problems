from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        current_seq, result = 1, 1
        seqs = [1]
        
        for i in range(1, len(nums)):
            if (nums[i] > nums[i-1]):
                current_seq += 1
            else:
                current_seq = 1
            seqs.append(current_seq)
            if (i - current_seq >= 0 and seqs[i-current_seq] >= current_seq):
                result = max(result, current_seq)
            else:
                result = max(result, current_seq // 2)
        return result
    
s = Solution()
print("Result", s.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))