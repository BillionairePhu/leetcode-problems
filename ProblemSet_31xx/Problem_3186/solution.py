from typing import Counter, List


class Solution:
  def maximumTotalDamage(self, power: List[int]) -> int:
    counter = Counter(power)
    keys = list(counter.keys())
    keys.sort()
    
    answer = Counter()
    result = 0
    for i in range(len(keys))[::-1]:
      key, considers = keys[i], []
      if (i+1<len(keys) and keys[i+1] > key+2):
        considers.append(answer[keys[i+1]])
      if (i+2<len(keys) and keys[i+2] > key+2):
        considers.append(answer[keys[i+2]])
      if (i+3<len(keys) and keys[i+3] > key+2):
        considers.append(answer[keys[i+3]])
      if (i+4<len(keys) and keys[i+4] > key+2):
        considers.append(answer[keys[i+4]])
      if (i+5<len(keys) and keys[i+5] > key+2):
        considers.append(answer[keys[i+5]])
      
      value = counter[key] * key
      if (len(considers) > 0):
        value += max(considers)
      
      answer[key] = value
      result = max(result, value)
    
    return max(answer.values())
    
  
s = Solution()
print(s.maximumTotalDamage([2,1,4,3,1,1,1,5]))
# print(s.maximumTotalDamage([1,1,3,4]))
# print(s.maximumTotalDamage([7,1,6,6]))
# print(s.maximumTotalDamage([7,1,6,3]))
# print(s.maximumTotalDamage([5,9,2,10,2,7,10,9,3,8]))