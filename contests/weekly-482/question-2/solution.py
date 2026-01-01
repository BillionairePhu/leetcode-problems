class Solution:
  def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
    final_cost = 0
    if (costBoth <= cost1 + cost2 and need1 > 0 and need2 > 0):
      common = min(need1, need2)
      final_cost += common * costBoth
      need1 -= common
      need2 -= common
      
    if (cost1 >= costBoth and need1 > 0):
      final_cost += need1 * costBoth
      need2 = max(0, need2 - need1)
      need1 = 0
      
    if (cost2 >= costBoth and need2 > 0):
      final_cost += need2 * costBoth
      need1 = max(0, need1 - need2)
      need2 = 0
    
    return final_cost + need1*cost1 + need2*cost2