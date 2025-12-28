from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms_earliest_available = [-1] * n
        meeting_counts = [0] * n
        meetings.sort(key=lambda x: x[0])
        
        for startTime, endTime in meetings:
            allocated = False
            for i in range(len(rooms_earliest_available)):
                if (rooms_earliest_available[i] <= startTime):
                    rooms_earliest_available[i] = endTime
                    meeting_counts[i] += 1
                    allocated = True
                    break
            if (allocated == True):
                continue
            earliest_available_room, earliest_available = 0, rooms_earliest_available[0]
            for i in range(len(rooms_earliest_available)):
                if (rooms_earliest_available[i] < earliest_available):
                    earliest_available = rooms_earliest_available[i]
                    earliest_available_room = i
            rooms_earliest_available[earliest_available_room] += (endTime - startTime)
            meeting_counts[earliest_available_room] += 1
        
        return meeting_counts.index(max(meeting_counts))
    
s = Solution()
print("Result", s.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))
print("Result", s.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))