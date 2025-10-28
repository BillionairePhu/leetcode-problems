from bisect import bisect_left, bisect_right
from typing import Counter, List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        result = 0
        frequencies = Counter(nums)
        freq_keys = list(frequencies.keys())
        freq_keys.sort()
        
        prefixes = [0]
        key_index_dict = {}
        for key in freq_keys:
            key_index_dict[key] = len(prefixes)
            prefixes.append(prefixes[-1] + frequencies[key])
        print(prefixes)

        for i in range(len(freq_keys)):
            key = freq_keys[i]
            upper, lower = key + k, key - k
            curr_index = key_index_dict[key]
            lower_index = bisect_left(freq_keys, lower)
            upper_index = bisect_right(freq_keys, upper)
            
            total_freq = prefixes[upper_index] - prefixes[lower_index]
            curr_freq = prefixes[curr_index] - prefixes[curr_index-1]
            freq = min(curr_freq + numOperations, total_freq)
            print("Key", key, "Total", total_freq, "Curr", curr_freq)
            print(upper, lower)
            result = max(result, freq)
        return result

s = Solution()
# print("Result", s.maxFrequency([5,11,20,20], 5, 1))
# print("Result", s.maxFrequency([9], 0, 0))
# print("Result", s.maxFrequency([2, 49], 97, 0))
print("Result", s.maxFrequency([88, 53], 27, 2))