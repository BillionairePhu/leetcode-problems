import math


class Solution:
    def minimumAbsDifference(arr: list[int]):
        arr.sort()
        result = math.inf
        resultArr = []
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1] <  result):
                result = arr[i] - arr[i-1]
                resultArr = [[arr[i-1], arr[i]]]
            elif (arr[i] - arr[i-1] == result):
                resultArr.append([arr[i-1], arr[i]])
        return resultArr