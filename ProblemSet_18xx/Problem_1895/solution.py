from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix_row = [[0] * (n+2) for _ in range(m+2)]
        prefix_col = [[0] * (n+2) for _ in range(m+2)]
        prefix_up_diag = [[0] * (n+2) for _ in range(m+2)]
        prefix_down_diag = [[0] * (n+2) for _ in range(m+2)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix_row[i][j] = prefix_row[i][j-1] + grid[i-1][j-1]
                prefix_col[i][j] = prefix_col[i-1][j] + grid[i-1][j-1]
                prefix_up_diag[i][j] = prefix_up_diag[i-1][j+1] + grid[i-1][j-1]
                prefix_down_diag[i][j] = prefix_down_diag[i-1][j-1] + grid[i-1][j-1]
        
        def check_if_magic_square(i, j, size: int) -> bool:
            one_sum = prefix_row[i+1][j+size] - prefix_row[i+1][j]
            for k in range(i, i+size):
                if (prefix_row[k+1][j+size] - prefix_row[k+1][j] != one_sum):
                    return False
            for k in range(j, j+size):
                if (prefix_col[i+size][k+1] - prefix_col[i][k+1] != one_sum):
                    return False
            sum_up_diag = prefix_up_diag[i+size][j+1] - prefix_up_diag[i][j+size+1]
            sum_down_diag = prefix_down_diag[i+size][j+size] - prefix_down_diag[i][j]
            print(sum_up_diag, sum_down_diag)
            
            if (sum_up_diag != one_sum or sum_down_diag != one_sum):
                return False
            return True
            
        
        size = min(m, n)
        while (size > 1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    print(i, j)
                    if (check_if_magic_square(i, j, size)):
                        return size
            size -= 1
        return size
                
            
s = Solution()
print("Result", s.largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))
# print("Result", s.largestMagicSquare([[1,9,3,5,5,8,1,6,9],[4,1,1,6,8,3,5,7,6],[9,8,4,7,2,4,9,2,7],[1,9,8,10,5,10,1,6,3]]))