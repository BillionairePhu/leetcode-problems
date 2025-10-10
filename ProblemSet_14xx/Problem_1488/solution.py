from typing import List


class Solution:
  def findFirstDryDay(self, dry_days: list[list[int]], start_day: int, end_day: int) -> int | None:
    for j in range(start_day // (10**2), (end_day // (10**2)) + 1):
      if (len(dry_days[j]) == 0):
        continue
      for dry_day in dry_days[j]:
        if (dry_day < start_day or dry_day > end_day):
          continue
        return dry_day
    return None
  
  def avoidFlood(self, rains: List[int]) -> List[int]:
    ans = []
    full_lakes = {}
    dry_days = [[] for i in range(10**3)]
    
    for i, rain in enumerate(rains):
      if (rain == 0):
        ans.append(0)
        dry_days[i // (10**2)].append(i)
      elif (rain not in full_lakes):
        ans.append(-1)
        full_lakes[rain] = i
      else:
        # print(i, rain, full_lakes[rain])
        # print(dry_days[0])
        
        dry_day = self.findFirstDryDay(dry_days, full_lakes[rain], i)
        if (dry_day == None):
          return []
        ans[dry_day] = rain
        dry_days[dry_day // (10**2)].remove(dry_day)
        
        full_lakes[rain] = i
        ans.append(-1)
    
    return [(val if val != 0 else 1) for val in ans]

s = Solution()
print(s.avoidFlood([1,2,3,4]))
print(s.avoidFlood([1,2,0,0,2,1]))
print(s.avoidFlood([1,2,0,1,2]))
print(s.avoidFlood([1,2,0,2,3,0,1]))
print(s.avoidFlood([0,1,1]))
print(s.avoidFlood([3,0,0,1,2,0,0,1,3,2]))