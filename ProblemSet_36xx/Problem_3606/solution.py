import re
from typing import List


class Solution:
  def validateCoupons(self,
      code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
    valid_indices = []
    
    for i in range(len(code)):
      if (not bool(re.fullmatch(r"[A-Za-z0-9_]+", code[i]))):
        print('a')
        continue
      if (businessLine[i] not in ["electronics", "grocery", "pharmacy", "restaurant"])  :
        continue
      if (not isActive[i]):
        continue
      valid_indices.append(i)
    
    valid_indices.sort(key=lambda x: (businessLine[x], code[x]))
    return [code[x] for x in valid_indices]
  
s = Solution()
print("Result", s.validateCoupons(
  code = ["SAVE20","","PHARMA5","SAVE@20"],
  businessLine = ["restaurant","grocery","pharmacy","restaurant"],
  isActive = [True,True,True,True]))