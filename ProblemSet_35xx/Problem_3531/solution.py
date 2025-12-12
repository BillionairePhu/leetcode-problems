from typing import List


class Solution:
  def countCoveredBuildings(
      self, n: int, buildings: List[List[int]]
    ) -> int:
    result = 0
    rows, columns = {}, {}
    for x, y in buildings:
      if (x not in columns):
        columns[x] = {"maxi": y, "mini": y}
      else:
        columns[x]["maxi"] = max(columns[x]["maxi"], y)
        columns[x]["mini"] = min(columns[x]["mini"], y)
        
      if (y not in rows):
        rows[y] = {"maxi": x, "mini": x}
      else:
        rows[y]["maxi"] = max(rows[y]["maxi"], x)
        rows[y]["mini"] = min(rows[y]["mini"], x)
    
    for x, y in buildings:
      if (x > rows[y]["mini"] and x < rows[y]["maxi"] and
          y > columns[x]["mini"] and y < columns[x]["maxi"]):
        result += 1
    return result

s = Solution()
# print("Result", s.countCoveredBuildings(3, [[1,2],[2,2],[3,2],[2,1],[2,3]]))
print("Result", s.countCoveredBuildings(5, [[1,3],[3,2],[3,3],[3,5],[5,3]]))