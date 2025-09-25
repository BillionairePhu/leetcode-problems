from typing import Counter


class Solution:
  def maxFreqSum(self, s: str) -> int:
    counter = Counter(s)
    max_vowels, max_consonants = 0, 0
    vowels = {"a", "i", "e", "o", "u"}
    for key, value in counter.items():
      if (key in vowels):
        max_vowels = max(max_vowels, value)
      else:
        max_consonants = max(max_consonants, value)
    return max_vowels + max_consonants
        
      
s = Solution()
print(s.maxFreqSum("successes"))