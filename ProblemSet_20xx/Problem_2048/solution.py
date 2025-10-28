from typing import Counter


class Solution:
  def nextBeautifulNumber(self, n: int) -> int:
    def isBalanced(n: int) -> bool:
      freqs = Counter(str(n))
      for key, value in freqs.items():
        if (int(key) != value):
          return False
      return True
    while True:
      if (isBalanced(n+1)):
        break
      n += 1
    return n+1

s = Solution()
print(s.nextBeautifulNumber(1))