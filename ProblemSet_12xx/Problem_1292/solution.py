from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        prefixSum = [
            [0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)
        ]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                prefixSum[i+1][j+1] = (prefixSum[i][j+1] +
                    prefixSum[i+1][j] - prefixSum[i][j] + mat[i][j])
                
        for row in prefixSum:
            print(row)
            
        def calculateSum(topLeftRow: int, topLeftCol: int, size: int) -> int:
            if (size == 0):
                return 0
            
            bottomRightRow = topLeftRow + size - 1
            bottomRightCol = topLeftCol + size - 1
            
            return (prefixSum[bottomRightRow+1][bottomRightCol+1]
                - prefixSum[bottomRightRow+1][topLeftCol]
                - prefixSum[topLeftRow][bottomRightCol+1]
                + prefixSum[topLeftRow][topLeftCol])
        
        result = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                curr = result
                while (i + curr - 1 < len(mat) and j + curr - 1 < len(mat[0]) and
                       calculateSum(i, j, curr) <= threshold):
                    result = max(result, curr)
                    curr += 1
        return result
            
s = Solution()
print("Result", s.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4))
print("Result", s.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 1))
print("Result", s.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 100))