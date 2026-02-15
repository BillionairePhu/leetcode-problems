class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        matrix = [[0] * 100 for _ in range(100)]
        
        for row in range(query_row+1):
            for col in range(row+1):
                if (row == 0):
                    matrix[row][col] = poured
                else:
                    if (col > 0 and matrix[row-1][col-1] > 1):
                        matrix[row][col] += (matrix[row-1][col-1] - 1) / 2
                    if (col <= row-1 and matrix[row-1][col] > 1):
                        matrix[row][col] += (matrix[row-1][col] - 1) / 2
                # print(row, col, matrix[row][col])
                if (row == query_row and col == query_glass):
                    return min(matrix[row][col], 1)
        return -1
    
s = Solution()
# print("Result", s.champagneTower(1,1,1))
# print("Result", s.champagneTower(2,1,1))
# print("Result", s.champagneTower(100000009,33,17))
print("Result", s.champagneTower(4,2,1))
print("Result", s.champagneTower(4,2,2))