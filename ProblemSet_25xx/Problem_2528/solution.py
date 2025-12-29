from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        coverage = []
        curr_coverage = sum(stations[:r+1])
        for index, station in enumerate(stations):
            coverage.append(curr_coverage)
            if (index - r >= 0):
                curr_coverage -= stations[index-r]
            if (index + r + 1 < len(stations)):
                curr_coverage += stations[index+r+1]
                
        def check_if_minimum_power_possible(power: int) -> bool:
            f_coverage = coverage.copy()
            diff = []
            extra = k
            curr_diff = 0
            for index, curr_coverage in enumerate(f_coverage):
                curr_power = curr_coverage + curr_diff
                # print(index, curr_power)
                if (power - curr_power > extra):
                    return False
                elif curr_power < power:
                    extra -= power - curr_power
                    curr_diff += power - curr_power
                    diff.append(power - curr_power)
                else:
                    diff.append(0)
                
                if (index - 2*r >= 0):
                    curr_diff -= diff[index - 2*r]
            return True
        
        # print(coverage)
        # print(check_if_minimum_power_possible(5))
        
        high = 10**11
        low = 0
        while low < high:
            mid = (low + high + 1) // 2
            if check_if_minimum_power_possible(mid):
                low = mid
            else:
                high = mid - 1
        return low
        
s = Solution()
# print("Result", s.maxPower([1,2,4,5,0], 1, 2))
print("Result", s.maxPower([4,4,4,4], 0, 3))