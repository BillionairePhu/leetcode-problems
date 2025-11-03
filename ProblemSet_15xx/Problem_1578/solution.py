from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time, last_color, last_time = 0, "", 0
        for i in range(len(colors)):
            if (colors[i] != last_color):
                last_color = colors[i]
                last_time = neededTime[i]
            else:
                time += min(last_time, neededTime[i])
                last_time = max(last_time, neededTime[i])
        return time
s = Solution()
print("Result", s.minCost("aabaa", [1,2,3,4,1]))