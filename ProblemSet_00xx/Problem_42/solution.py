from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        stack = [[-1, 0]]
        for curr_poss, curr_height in enumerate(height):
            last_pos, last_height = stack.pop()
            base = last_height
            
            while curr_height > last_height and last_pos != -1:
                water += (curr_poss - last_pos - 1) * (min(last_height, curr_height) - base)
                base = last_height
                last_pos, last_height = stack.pop()
            
            
            if last_pos != -1:
                water += (curr_poss - last_pos - 1) * (min(last_height, curr_height) - base)
                
            stack.append([last_pos, last_height])
            stack.append([curr_poss, curr_height])
        return water
    
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))