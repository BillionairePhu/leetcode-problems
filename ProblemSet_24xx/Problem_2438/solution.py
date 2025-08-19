# Write your solution here
from typing import List


class Solution:
    modulo = 10 ** 9 + 7
    def productQueries(
            self, n: int, queries: List[List[int]]
        ) -> List[int]:
        powers, results, i = [0], [], 0
        while n > 0:
            if (n & (1 << i) != 0):
                powers.append(powers[-1] + i)
                n -= (1 << i)
            i += 1
        for query in queries:
            results.append(pow(2, powers[query[1]+1] - powers[query[0]], self.modulo))
            
        return results

s = Solution()
print("Result",s.productQueries(15, [[0,1],[2,2],[0,3]]))