from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        prev_point = points[0]
        for point in points:
            delta_x = abs(point[0] - prev_point[0])
            delta_y = abs(point[1] - prev_point[1])
            result += max(delta_x, delta_y)
            prev_point = point
        return result

s = Solution()
print("Result", s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))