from typing import List


class Solution:
  def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
    result = 0
    
    startRow, startCol = startPos
    homeRow, homeCol = homePos
    
    if (startRow < homeRow):
      result += sum(rowCosts[startRow+1:homeRow+1])
    else:
      result += sum(rowCosts[homeRow:startRow])
      
    if (startCol < homeCol):
      result += sum(colCosts[startCol+1:homeCol+1])
    else:
      result += sum(colCosts[homeCol:startCol])
    
    return result

s = Solution()
print(s.minCost(
  [5,5],
  [5,2],
  [7,1,3,3,5,3,22,10,23],
  [5,5,6,2,0,16]
))