class Solution:
  def doesAliceWin(self, s: str) -> bool:
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for char in s:
      if char in vowels:
        count += 1
        return True
    return False
  
s = Solution()
print(s.doesAliceWin("leetcoder"))