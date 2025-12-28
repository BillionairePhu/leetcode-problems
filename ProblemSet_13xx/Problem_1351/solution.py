import bisect
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        boundary_index = bisect.bisect_right(grid[0], 0, key=lambda x: -x)
        # print(boundary_index)
        result = 0
        
        for row in grid:
            while (row[boundary_index-1] < 0 and boundary_index > 0):
                boundary_index -= 1
            result += (len(grid[0]) - boundary_index)
            print(row, boundary_index, result)
        return result
    
s = Solution()
# print("Result", s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
# print("Result", s.countNegatives([[3,2],[1,0]]))
print("Result", s.countNegatives([[5,1,0],[-5,-5,-5]]))