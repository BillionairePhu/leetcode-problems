from typing import List


class Solution:
  def countPermutations(self, complexity: List[int]) -> int:
    first, modulo = complexity[0], 10**9 + 7
    count, result = 0, 1
    
    for i in range(1, len(complexity)):
      if (complexity[i] < first):
        return 0
      count += 1
    
    for i in range(2, count+1):
      result = (result * i) % modulo
    
    return result
    