from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_combos: dict[str, list[str]] = {}
        
        for allowed_combo in allowed:
            key, value = allowed_combo[:2], allowed_combo[2]
            if (key not in allowed_combos):
                allowed_combos[key] = []
            allowed_combos[key].append(value)
        
        def get_possible_combs(a: str) -> set[str]:
            if (len(a) == 2):
                if (a in allowed_combos):
                    return set(allowed_combos[a])
                else:
                    return set()
            key, ans = a[:2], set()
            if (key not in allowed_combos):
                return set()
            for val in allowed_combos[key]:
                for sub_combo in get_possible_combs(a[1:]):
                    ans.add(val + sub_combo)
            return ans
        
        prev = set([bottom])
        for _ in range(len(bottom)-1):
            curr = set()
            for comb in prev:
                child_combs = get_possible_combs(comb)
                curr = curr.union(child_combs)
            prev = curr
        
        return len(prev) > 0
        
s = Solution()
# print("Result", s.pyramidTransition("BCD", ["BCC","CDE","CEA","FFF"]))
print("Result", s.pyramidTransition("AAAA", ["AAB","AAC","BCD","BBE","DEF"]))
