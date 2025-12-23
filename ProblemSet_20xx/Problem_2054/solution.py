from typing import List
from bisect import bisect_left


class Solution:
  def maxTwoEvents(self, events: List[List[int]]) -> int:
    events.sort(key = lambda x: x[1])
    dp_values = [0]
    time_frames = []
    result = 0
    
    for start_time, end_time, value in events:
      index = bisect_left(time_frames, start_time)
      prev_value  = dp_values[index]
        
      if (not time_frames or time_frames[-1] != end_time):
        time_frames.append(end_time)
        dp_values.append(max(dp_values[-1], value))
      else:
        dp_values[-1] = max(dp_values[-1], value)
      result = max(result, prev_value + value)
      
    return result

# print(bisect_right([5],4))
s = Solution()
# print("Result", s.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))
# print("Result", s.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5], [7,8,1],[9,10,2]]))
# print("Result", s.maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]))
print("Result", s.maxTwoEvents([[10,83,53],[63,87,45],[97,100,32],[51,61,16]]))