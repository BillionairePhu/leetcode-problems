from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
        ) -> int:
        free_times, meetings = [], []
        time = 0
        top_3_freetime = [0,0,0]
        top_3_index = [-1,-1,-1]
        
        for i in range(len(startTime)):
            free_times.append(startTime[i] - time)
            least_top_3 = min(top_3_freetime)
            if (startTime[i] - time > least_top_3):
                index = top_3_freetime.index(least_top_3)
                top_3_freetime[index] = startTime[i] - time
                top_3_index[index] = i
            
            meetings.append(endTime[i] - startTime[i])
            
            time = endTime[i]
        free_times.append(eventTime - time)
        least_top_3 = min(top_3_freetime)
        if (eventTime - time > least_top_3):
            index = top_3_freetime.index(least_top_3)
            top_3_freetime[index] = eventTime - time
            top_3_index[index] = len(startTime)
            
        sum, result = 0, 0
        for i in range(0, len(free_times)-1):
            sum = free_times[i] + free_times[i+1]
            for j in range(3):
                if (top_3_freetime[j] >= meetings[i] and top_3_index[j] != i and top_3_index[j] != i+1):
                    sum = free_times[i] + free_times[i+1] + meetings[i]
                    break
            if (sum > result):
                result = sum
                
        return result
            
            
        
s = Solution()
print('Result', s.maxFreeTime(5, [0,1,2,3,4], [1,2,3,4,5]))
print('Result', s.maxFreeTime(41, [17, 24], [19,25]))