from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        last_two_selected = [intervals[0][1], intervals[0][1]-1]
        ans = 2
        
        for start, end in intervals:
            new_selected_count = 0
            for i in range(len(last_two_selected)):
                if not (start <= last_two_selected[i] <= end):
                    last_two_selected[i] = end - new_selected_count
                    new_selected_count += 1
                    ans += 1
            print(start, end, last_two_selected)
        return ans
    
s = Solution()
print("Result", s.intersectionSizeTwo([[1,3],[3,7],[5,7],[7,8]]))