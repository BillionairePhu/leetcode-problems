from typing import List

def gcd(a: int, b: int):
    while (a != 0 and b != 0):
        if (a > b):
            a = a % b
        else:
            b = b % a
    return a | b
                    
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        gcds = [nums[0]]
        count = 10**6
        
        for i in range(len(nums)-1):
            # print("GCD", gcds)
            if (nums[i+1] == 1):
                count = 0
                break
            
            new_gcds = []
            
            for j in range(len(gcds)):
                curr_gcd = gcd(gcds[j], nums[i+1])
                if (curr_gcd == 1):
                    count = min(count, len(gcds) - j)
                new_gcds.append(curr_gcd)
            
            new_gcds.append(nums[i+1])
            gcds = new_gcds
            
        if (count == 0 or nums[0] == 1):
            return [num == 1 for num in nums].count(False)
        
        return -1 if count == 10**6 else len(nums) + count - 1
        
s = Solution()
# print('Result', s.minOperations([2,6,3,4]))
print('Result', s.minOperations([2,10,6,14]))
# print('Result', s.minOperations([4,2,6,3]))
# print('Result', s.minOperations([1,1]))
# print('Result', s.minOperations([1,2]))
        
# print("GCD", gcd(6, 10))