import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [[grid[0][0], 0, 0]]
        traversed = set()
        level = 0
        while level < len(grid) * len(grid[0]):
            
            while (heap[0][0] <= level):
                curr_level, i, j = heapq.heappop(heap)
                traversed.add((i, j))
                if (i == len(grid)-1 and j == len(grid[0])-1):
                    return level
                
                if (i > 0 and (i-1, j) not in traversed):
                    heapq.heappush(heap, [grid[i-1][j], i-1, j])
                if (j > 0 and (i, j-1) not in traversed):
                    heapq.heappush(heap, [grid[i][j-1], i, j-1])
                if (i < len(grid)-1 and (i+1, j) not in traversed):
                    heapq.heappush(heap, [grid[i+1][j], i+1, j])
                if (j < len(grid)-1 and (i, j+1) not in traversed):
                    heapq.heappush(heap, [grid[i][j+1], i, j+1])
                    
            level += 1
        return None

s = Solution()
print(s.swimInWater([[0,2],[1,3]]))
print(s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))