from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row_length = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        result = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == "0"):
                    continue
                curr_row_length = 1 if (j == 0) else row_length[i][j-1] + 1
                row_length[i][j] = curr_row_length
                
                number_of_row = 0
                for k in range(i, -1, -1):
                    number_of_row += 1
                    curr_row_length = min(curr_row_length, row_length[k][j])
                    if (curr_row_length == 0):
                        break
                    size = number_of_row * curr_row_length
                    result = max(size, result)
        
        return result
    
s = Solution()
print("Result", s.maximalRectangle([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]]))
print("Result", s.maximalRectangle(
    [["0"]]
))
print("Result", s.maximalRectangle(
    [["1"]]
))

# a * b >= c * d
# (a+1) * (b+1) ? (c+1) * (d+1)
# a + b ? c + d