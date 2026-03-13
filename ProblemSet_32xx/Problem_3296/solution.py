import heapq
from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap: list[list[int]] = []
        for index, workerTime in enumerate(workerTimes):
            heapq.heappush(heap, (workerTime, workerTime, 1, index))
        
        time = [0] * len(workerTimes)
        while mountainHeight > 0:
            currTime, workerTime, multiplier, index = heapq.heappop(heap)
            
            doneTime = currTime + workerTime * (multiplier + 1)
            heapq.heappush(heap, (doneTime, workerTime, multiplier + 1, index))
            time[index] = currTime
            
            mountainHeight -= 1
            
        return max(time)
    
s = Solution()
print("Result", s.minNumberOfSeconds(4, [2, 1, 1]))
# print("Result", s.minNumberOfSeconds(10, [3, 2, 4]))
print("Result", s.minNumberOfSeconds(5, [1]))
print("Result", s.minNumberOfSeconds(10, [3, 2, 2, 4]))