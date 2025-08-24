class Solution:
  def gcdOfOddEvenSums(self, n: int) -> int:
    sumEven, sumOdd = 0, 0
    for i in range(2*n+1):
      sumOdd = sumOdd + i if i & 1 == 1 else sumOdd
      sumEven = sumEven + i if i & 1 == 0 else sumEven
      
    for i in range(sumEven)[::-1]:
      if (sumOdd % i == 0 and sumEven % i == 0):
        return i