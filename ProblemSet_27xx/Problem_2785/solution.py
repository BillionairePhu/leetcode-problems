import string
from typing import Counter


class Solution:
  def sortVowels(self, s: str) -> str:
    vowels = {
      "a", "i", "e", "o", "u", "A", "I", "E", "O", "U"
    }
    counter = Counter(s)
    vowels = list(vowels)
    vowels.sort()
    index = 0
    t = ""
    for char in s:
      if char in vowels:
        while counter[vowels[index]] == 0:
          index += 1
        t += vowels[index]
        counter[vowels[index]] -= 1
      else:
        t += char
    return t
        
s = Solution()
print(s.sortVowels("lEetcOde"))
    