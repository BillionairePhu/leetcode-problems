from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        counts = [
            [
                [0]*k for j in range(len(grid[0])) 
            ] for i in range(len(grid))
        ]
        
        first_cell_mod = grid[0][0] % k
        counts[0][0][first_cell_mod] = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr_cell = counts[i][j]
                curr_value = grid[i][j]
                
                # Add paths originating from left cell
                if (j > 0):
                    left_cell = counts[i][j-1]
                    for modulo in range(k):
                        curr_cell[(modulo + curr_value) % k] += left_cell[modulo]
                        curr_cell[(modulo + curr_value) % k] %= (10**9 + 7)
                
                # Add paths originating from top cell
                if (i > 0):
                    top_cell = counts[i-1][j]
                    for modulo in range(k):
                        curr_cell[(modulo + curr_value) % k] += top_cell[modulo]
                        curr_cell[(modulo + curr_value) % k] %= (10**9 + 7)
                
        return counts[-1][-1][0]
                