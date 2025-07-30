import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        maxHeap, minHeap = [], []
        
        for i in range(n):
            heapq.heappush(maxHeap, -nums[i])
            heapq.heappush(minHeap, nums[2*n+i])
        
        left = [-sum(maxHeap)]
        right = [sum(minHeap)]
        for i in range(0, n):
            # Calculate left side
            heapq.heappush(maxHeap, -nums[n+i])
            sum_left = left[-1] + (nums[n+i])
            sum_left += heapq.heappop(maxHeap)
            left.append(sum_left)
                
            # Calculate right side
            heapq.heappush(minHeap, nums[2*n-1-i])
            sum_right = right[-1] + (nums[2*n-1-i])
            sum_right -= heapq.heappop(minHeap)
            right.append(sum_right)
            
        result = [(left[i] - right[n-i]) for i in range(n+1)]
        return min(result)
    
s = Solution()
print('Result', s.minimumDifference([7,9,5,8,1,3]))