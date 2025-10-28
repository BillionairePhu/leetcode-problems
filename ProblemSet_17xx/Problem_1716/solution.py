class Solution:
  def totalMoney(self, n: int) -> int:
    money, result = 0, 0
    for i in range(n):
      if (i % 7 == 0):
        money += 1
      result += (money + i % 7)
    return result
  
s = Solution()
print("Result", s.totalMoney(4))
print("Result", s.totalMoney(10))
print("Result", s.totalMoney(20))