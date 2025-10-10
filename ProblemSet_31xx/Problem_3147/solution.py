from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        enery_obtained = [0 for _ in range(k)]
        for i in range(len(energy)):
            enery_obtained[i % k] = max(enery_obtained[i % k] + energy[i], energy[i])
        return max(enery_obtained)
    
s = Solution()
print(s.maximumEnergy([5,2,-10,-5,1], 3))
print(s.maximumEnergy([-2,-3,-1], 2))