class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    result = numBottles
    
    while numBottles >= numExchange:
      newBottles = numBottles // numExchange
      
      result += newBottles
      
      numBottles = newBottles + (numBottles % numExchange)
    
    return result