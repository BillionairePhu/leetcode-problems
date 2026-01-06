from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = 0
        neg_count = 0
        zero_count = 0
        min_abs_ele = abs(matrix[0][0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result += abs(matrix[i][j])
                min_abs_ele = min(min_abs_ele, abs(matrix[i][j]))
                if (matrix[i][j] < 0):
                    neg_count += 1
                elif (matrix[i][j] == 0):
                    zero_count += 1
        
        if (neg_count % 2 == 1 and zero_count == 0):
            return result - 2 * min_abs_ele
        else:
            return result
        
s = Solution()
# print("result", s.maxMatrixSum([[1,-1],[-1,1]]))
print("result", s.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))
                