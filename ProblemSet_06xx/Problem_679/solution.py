from typing import List
import itertools

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        perms = list(itertools.permutations(cards))
        final = set()
        for perm in perms:
            final = final.union(self.calculate(list(perm)))
        for value in final:
            if abs(value-24) < 0.0001:
                return True
        return False
    
    def calculate(self, cards: list) -> set:
        result = set()
        if (len(cards) == 1):
            return set(cards[0])
        
        # Interact with the next number
        nums = self.interact(cards[0], cards[1])
        if (len(cards) == 2):
            return nums
        for num in nums:
            temps = self.calculate([num] + cards[2:])
            for temp in temps:
                result.add(temp)
            
        # Interact with the next group values
        for i in range(2, len(cards)):
            values = self.calculate(cards[1:i+1])
            for value in values:
                nums = self.interact(cards[0], value)
                for num in nums:
                    if (i+1 < len(cards)):
                        result = result.union(self.calculate([num] + cards[i+1:]))
                    else:
                        result.add(num)
        return result
        
    def interact(self, a:int, b:int) -> set:
        result = set()
        result.add(a + b)
        result.add(a - b)
        result.add(a * b)
        if (b != 0):
            result.add(a / b)
        return result

s = Solution()
print(s.judgePoint24([3,3,8,8]))
# print(s.judgePoint24([8,4,7,1]))
# print(s.judgePoint24([1,2,1,2]))