class Solution:
  def largestGoodInteger(self, num: str) -> str:
    result = -1
    
    for i in range(len(num)-2):
      curr = int(num[i:i+3])
      if (curr % 111 == 0 and curr > result):
        result = curr
    
    return "" if result == -1 else str(result)