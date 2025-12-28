from typing import Counter, List
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        self.curr = 0
        large = SortedList()
        small = SortedList()
        freqs = Counter(nums[:k])
        result = []
        
        def insert_to(value: int, key: int):
            if (len(large) < x or large[0] < (value, key)):
                large.add((value, key))
                self.curr += value * key
                if (len(large) > x):
                    removed = large.pop(0)
                    small.add(removed)
                    self.curr -= removed[0] * removed[1]
            else:
                small.add((value, key))
        
        def remove(value: int, key: int):
            if ((value, key) in large):
                large.remove((value, key))
                self.curr -= value * key
                if (len(small) > 0):
                    replaced = small.pop()
                    large.add(replaced)
                    self.curr += replaced[0] * replaced[1]
            else:
                small.remove((value, key))
        
        for key, value in freqs.items():
            insert_to(value, key)
        
        for i in range(len(nums) - k + 1):
            result.append(self.curr)
            
            if (i == len(nums) - k):
                break
            added_num = nums[i+k]
            added_freq = freqs[added_num]
            if (added_freq > 0):
                remove(added_freq, added_num)
            freqs[added_num] += 1
            insert_to(added_freq+1, added_num)
            
            decreased_num = nums[i]
            decreased_freq = freqs[decreased_num]
            remove(decreased_freq, decreased_num)
            freqs[decreased_num] -= 1
            insert_to(decreased_freq-1, decreased_num)
        return result
                
s = Solution()
# print("Result", s.findXSum([1,1,2,2,3,4,1,1], 6, 2))  
print("Result", s.findXSum([3,8,7,8,7,5], 2, 2))  