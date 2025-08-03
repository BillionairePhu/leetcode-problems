# Write your solution here
from typing import Counter, List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        basket1_counter = Counter(basket1)
        basket2_counter = Counter(basket2)
        counter = basket1_counter + basket2_counter
        
        swap = []
        min_key = min(counter.keys())
        for key in counter.keys():
            if (counter[key] % 2 != 0):
                return -1
            freq = counter[key] // 2
            diff = freq - basket1_counter[key]
            swap += [key] * abs(diff)
        swap.sort()
        
        result = 0
        for value in swap[0:len(swap)//2]:
            if value > min_key * 2:
                result += 2 * min_key
            else:
                result += value
        return result
    
s = Solution()
print('Result', s.minCost(
    [84,80,43,8,80,88,43,14,100,88],
    [32,32,42,68,68,100,42,84,14,8]))