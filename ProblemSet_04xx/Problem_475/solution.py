from typing import List


class Solution:
  def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    houses.sort()
    heaters.sort()
    
    heater_index, result = 0, 0
    for house in houses:
      while (heater_index + 1 < len(heaters)
             and heaters[heater_index + 1] <= house):
        heater_index += 1
      radius = min(abs(house - heaters[heater_index]), abs(heaters[heater_index + 1] - house)) \
        if heater_index + 1 < len(heaters) else abs(house - heaters[heater_index])
      result = max(result, radius)
    return result

s = Solution()
# print("Result", s.findRadius([1,2,3,4], [1,4]))
print("Result", s.findRadius([1,5], [10]))