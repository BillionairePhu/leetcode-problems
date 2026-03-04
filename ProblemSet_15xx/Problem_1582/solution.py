from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            row = mat[i]
            index, violated = -1, False
            for j in range(len(row)):
                if (row[j] == 1):
                    if (index == -1):
                        index = j
                    else:
                        violated = True
                        break
            if not (index != -1 and not violated):
                continue
            for j in range(len(mat)):
                if (mat[j][index] == 1 and j != i):
                    violated = True
                    break
            if (not violated):
                result += 1
        return result
    
s = Solution()
print("Result", s.numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
print("Result", s.numSpecial([
    [1,0,0],
    [0,1,0],
    [0,0,1]]))
# print("Result", s.numSpecial([
#     [0,0,1,0],
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,1,0,0]]))