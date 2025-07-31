# Write your solution here
from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result, curr_set = set(), set()
        
        for num in arr:
            new_set = set()
            
            for ele in curr_set:
                new_set.add(ele | num)
                result.add(ele | num)
            new_set.add(num)
            curr_set = new_set
            
            result.add(num)
        return len(result)
    
s = Solution()
print(s.subarrayBitwiseORs([1,2,4]))