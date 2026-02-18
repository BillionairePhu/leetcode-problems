class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        state = None
        while n > 0:
            curr_state = n & 1
            if (curr_state == state):
                return False
            state = curr_state
            n >>= 1
        return True