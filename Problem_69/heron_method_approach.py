class Solution:
    def mySqrt(self, x: int) -> int:
        iterations = 100
        result = 1
        # Increase iteration to increase accuracky
        for _ in range(iterations):
            result = 0.5 * (result + x/result)
        return int(result) # Get the floored integer of the result