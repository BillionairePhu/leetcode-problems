class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # The constrainst says that the max number is 10^6, which is < than 2^29
        # so this set of primes is enough
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
        def countSetBit(num: int):
            count = 0
            while num > 0:
                if (num & 1 == 1):
                    count += 1
                num >>= 1
            return count
        
        result = 0
        for num in range(left, right+1):
            if countSetBit(num) in primes:
                result += 1
        return result