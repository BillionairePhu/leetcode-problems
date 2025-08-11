from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        modulo, power, nums = 10**9 + 7, 1, []
        while n > 0:
            print(n)
            pNum = 2 ** power
            if (n % pNum != 0):
                nums.append(power-1)
                n -= 2 ** (power-1)
            if (pNum > n):
                break
            power += 1
        prefixes = [0]
        for i in range(len(nums)):
            prefixes.append(prefixes[-1] + nums[i])
        results = []
        for start, end in queries:
            results.append(
                pow(2, prefixes[end+1] - prefixes[start], modulo)
                )
        return results
    
s = Solution()
print("Result", s.productQueries(15, [[0,1],[2,2],[0,3]]))