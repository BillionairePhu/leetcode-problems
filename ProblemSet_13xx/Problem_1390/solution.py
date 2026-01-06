from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        prime_numbers = []

        def isPrimeNumber(num: int) -> bool:
            for prime in prime_numbers:
                if prime * prime > num:
                    break
                if num % prime == 0:
                    return False
            return True

        for i in range(2, 1001):
            if isPrimeNumber(i):
                prime_numbers.append(i)

        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            for prime in prime_numbers:
                if prime * prime > num:
                    break
                if num % prime == 0:
                    return False
            return True

        result = 0

        for num in nums:
            # Case 1: p^3
            a = round(num ** (1/3))
            if a * a * a == num and is_prime(a):
                result += 1 + a + a * a + num
                continue

            # Case 2: p * q
            for prime in prime_numbers:
                if prime * prime > num:
                    break
                if num % prime == 0:
                    other = num // prime
                    if other != prime and is_prime(other):
                        result += 1 + prime + other + num
                    break

        return result
