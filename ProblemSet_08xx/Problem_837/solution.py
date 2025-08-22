class Solution:
  def new21Game(self, n: int, k: int, maxPts: int) -> float:
    if (k == 0):
      return 1
    unit, arrays = 1/maxPts, [1/maxPts if i < maxPts else 0  for i in range(n+maxPts)]
      
    i, s = 1, 0
    while i < n:
      if (i - 1 < k - 1):
        s += arrays[i - 1]
      if (i - maxPts - 1 >= 0 and i - maxPts - 1 < k - 1):
        s -= arrays[i - maxPts -1]
      arrays[i] += unit * s
      i += 1
    return sum(arrays[k-1:n])
  
s = Solution()
# print("Result", s.new21Game(10, 1, 10))
# print("Result", s.new21Game(6, 1, 10))
print("Result", s.new21Game(12, 1, 10))
# print("Result", s.new21Game(5710, 5070, 8516))
        