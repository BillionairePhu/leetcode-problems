class Solution:
    def reverseBits(self, n: int) -> int:
        bitString = bin(n)[2:]
        reversedBitStrin = bitString[::-1] + (32 - len(bitString)) * "0"
        return int(reversedBitStrin, 2)