class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        mod, mod_set = 1, set()
        for i in range(k):
            if (mod % k == 0):
                return i+1
            if (mod in mod_set):
                return -1
            mod_set.add(mod)
            mod = (mod * 10 + 1) % k
        return -1

s = Solution()
print(s.smallestRepunitDivByK(3))