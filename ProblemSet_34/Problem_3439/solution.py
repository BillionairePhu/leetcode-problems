from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
        ) -> int:
        free_times = []
        time = 0
        
        for i in range(len(startTime)):
            free_times.append(startTime[i] - time)
            time = endTime[i]
        free_times.append(eventTime - time)
            
        count, sum, result = 0, 0, 0
        for i in range(len(free_times)):
            if (count < k + 1):
                sum += free_times[i]
                count += 1
            else:
                sum += free_times[i]
                sum -= free_times[i-k-1]
            if (sum > result):
                result = sum
                
        return result
            
            
        
s = Solution()
print('Result', s.maxFreeTime(5, 1, [1,3], [2,5]))
print('Result', s.maxFreeTime(10, 1, [0,2,9], [1,4,10]))
print('Result', s.maxFreeTime(10, 1, [0,2,8], [1,4,9]))
print('Result', s.maxFreeTime(5, 2, [0,1,2,3,4], [1,2,3,4,5]))