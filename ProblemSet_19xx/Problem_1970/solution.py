from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        full_map = [[0] * col for _ in range(row)]
        
        def expand(i: int, j: int, visited: list[list[bool]]) -> bool:
            if (visited[i][j] == True or full_map[i][j] == 1):
                return False
            
            visited[i][j] = True
            if (i == row-1):
                return True
            
            if (i > 0):
                result = expand(i-1, j, visited)
                if result:
                    return True
            if (i < row-1):
                result = expand(i+1, j, visited)
                if result:
                    return True
            if (j > 0):
                result = expand(i, j-1, visited)
                if result:
                    return True
            if (j < col-1):
                result = expand(i, j+1, visited)
                if result:
                    return True
            return False
        
        def check_if_still_crossable():
            visited = [[False] * col for _ in range(row)]
            for i in range(col):
                result = expand(0, i, visited)
                if (result):
                    return True
            return False
        
        low = 0
        high = len(cells)
        while low < high:
            mid = (low + high + 1) // 2
            
            full_map = [[0] * col for _ in range(row)]
            for cell in cells[:mid]:
                cell_row = cell[0] - 1  
                cell_col = cell[1] - 1
                full_map[cell_row][cell_col] = 1
            
            if (check_if_still_crossable() == True):
                low = mid
            else:
                high = mid - 1
                
        return low
    
s = Solution()
print("Result", s.latestDayToCross(2, 2 , [[1,1],[2,1],[1,2],[2,2]]))
print("Result", s.latestDayToCross(2, 2 , [[1,1],[1,2],[2,1],[2,2]]))
print("Result", s.latestDayToCross(3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))
            
            