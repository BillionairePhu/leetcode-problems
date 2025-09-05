

class Solution:
  def makeTheIntegerZero(self, num1: int, num2: int) -> int:
    def count_ones(n: int) -> int:
      return bin(n).count('1')
    
    for i in range(1, 61):
      num = num1 - i * num2
      if (num > 0):
        ones = count_ones(num)
        # print(i, num, ones)
        if (ones <= i and i <= num):
          return i
    return -1
  
s = Solution()
print(s.makeTheIntegerZero(3, -2))
print(s.makeTheIntegerZero(5, 7))