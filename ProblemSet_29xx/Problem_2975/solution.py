from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
        ) -> int:
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        widths = set()
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                widths.add(abs(vFences[j] - vFences[i]))
        
        result = -1
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                print(result)
                if (abs(hFences[j] - hFences[i])) in widths:
                    print(abs(hFences[j] - hFences[i]))
                    result = max(result, abs(hFences[j] - hFences[i]))
                    
        return result ** 2 if result != -1 else result

s = Solution()
# print("Result", s.maximizeSquareArea(4, 3, [2,3], [2]))
print("Result", s.maximizeSquareArea(6, 7, [2], [4]))