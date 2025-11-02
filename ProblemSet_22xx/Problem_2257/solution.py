from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
        ) -> int:
        map = [[0] * n for _ in range(m)]
        
        for row, col in guards:
            map[row][col] = 1
        for row, col in walls:
            map[row][col] = 2
        
        def mark(i, j):
            # To the left
            row, col = i, j-1
            while col >= 0 and (map[row][col] == 0 or map[row][col] == -1):
                map[row][col] = -1
                col -= 1
            # To the right
            row, col = i, j+1
            while col < n and (map[row][col] == 0 or map[row][col] == -1):
                map[row][col] = -1
                col += 1
            # To the top
            row, col = i-1, j
            while row >= 0 and (map[row][col] == 0 or map[row][col] == -1):
                map[row][col] = -1
                row -= 1
            # To the right
            row, col = i+1, j
            while row < m and (map[row][col] == 0 or map[row][col] == -1):
                map[row][col] = -1
                row += 1
                
        
        for i in range(m):
            for j in range(n):
                if (map[i][j] == 1):
                    mark(i, j)
        
        result = 0
        for i in range(m):
            for j in range(n):
                if (map[i][j] == 0):
                    result += 1
        # for row in map:
        #     print(row)
        return result
        
s = Solution()
print(s.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))