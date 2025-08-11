from typing import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_sets = []
        for i in range(31):
            num = 2**i
            num_str = str(num)
            num_set = Counter(num_str)
            power_sets.append(num_set)
        n_set = Counter(str(n))
        return n_set in power_sets