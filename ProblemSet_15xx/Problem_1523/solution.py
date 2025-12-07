class Solution:
  def countOdds(self, low: int, high: int) -> int:
    range = high - low + 1
    return (range + 1) // 2 if low % 2 == 1 else range // 2
  
s = Solution()
print("Result", s.countOdds(3, 7))