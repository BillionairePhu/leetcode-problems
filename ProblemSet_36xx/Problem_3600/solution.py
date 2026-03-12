from math import inf
from typing import List


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: (-x[3], -x[2]))
        added_edges, groups = [], [i for i in range(n)]
        
        def find_group(num: int) -> int:
            if (groups[num] != num):
                group = find_group(groups[num])
                groups[num] = group
            return groups[num]
        
        for edge in edges:
            u, v, s, must = edge
            group_u = find_group(u)
            group_v = find_group(v)
            if (group_u != group_v):
                added_edges.append(edge)
                new_group = min(group_u, group_v)
                groups[group_u] = new_group
                groups[group_v] = new_group
            elif (must == 1):
                return -1
        
        for i in range(n):
            group = find_group(i)
            if (group != 0):
                return -1
        
        result = inf
        for edge in added_edges[::-1]:
            u, v, s, must = edge
            if (k > 0 and must == 0):
                result = min(result, s*2)
                k -= 1
            else:
                result = min(result, s)
        return result
    
s = Solution()
print("Result", s.maxStability(3, [[0,1,2,1],[1,2,3,0]], 1))
print("Result", s.maxStability(3, [[0,1,4,0],[1,2,3,0],[0,2,1,0]], 2))
print("Result", s.maxStability(3, [[0,1,1,1],[1,2,1,1],[2,0,1,1]], 0))