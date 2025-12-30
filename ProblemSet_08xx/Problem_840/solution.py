from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check_magic_square(m: int, n: int) -> bool:
            num_set = set()
            cols = [[], [], []]
            rows = [[], [], []]
            diags = [[], []]
            
            for i in range(3):
                for j in range(3):
                    if (grid[i+m][j+n] >= 10 or grid[i+m][j+n] == 0):
                        return False
                    num_set.add(grid[i+m][j+n])
                    cols[j].append(grid[i+m][j+n])
                    rows[i].append(grid[i+m][j+n])
                    if (i == j):
                        diags[0].append(grid[i+m][j+n])
                    if (i == 2-j):
                        diags[1].append(grid[i+m][j+n])
            if (len(num_set) != 9):
                return False
            for i in range(3):
                if (sum(cols[i]) != 15):
                    return False
                if (sum(rows[i]) != 15):
                    return False
            if (sum(diags[0]) != sum(diags[1])):
                return False
            return True
        
        result = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                result += 1 if check_magic_square(i, j) else 0
                
        return result

s = Solution()
# print("Result", s.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
print("Result", s.numMagicSquaresInside([[1,8,6],[10,5,0],[4,2,9]]))