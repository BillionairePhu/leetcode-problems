from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        def maxRightmostZeroBlock(row: list[int]):
            result = 0
            for i in range(len(row)-1, -1, -1):
                if (row[i] == 0):
                    result += 1
                else:
                    return result
            return result
        
        rows = [maxRightmostZeroBlock(row) for row in grid]
        colCount = len(grid[0])
        
        def swap(array: list[int], i: int, j: int):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        
        def replace(array: list[int], popped: int, inserted: int):
            for i in range(popped, inserted, -1):
                swap(array, i, i-1)
        
        ans = 0
        for i in range(len(rows)):
            for j in range(i, len(rows)):
                if (rows[j] >= colCount - i - 1):
                    replace(rows, j, i)
                    ans += j - i
                    break
                elif (j == len(rows) - 1):
                    return -1
        return ans
                    
        
                    
            
        
        
s = Solution()
print("Result", s.minSwaps([[0,0,1],[1,1,0],[1,0,0]]))
print("Result", s.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))
print("Result", s.minSwaps([[0,1,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0]]))
print("Result", s.minSwaps([[1,0,0],[1,1,0],[1,1,1]]))