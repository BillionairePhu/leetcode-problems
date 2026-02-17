from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def countOnBit(num: int) -> int:
            count = 0
            while num > 0:
                if (num & 1 == 1):
                    count += 1
                num >>= 1
            return count
        
        result = []
        for hour in range(12):
            hourOnBit = countOnBit(hour)
            if (hourOnBit > turnedOn):
                continue
            remainingBit = turnedOn - hourOnBit
            for minute in range(60):
                minuteOnBit = countOnBit(minute)
                if (minuteOnBit == remainingBit):
                    result.append(str(hour) + ":" + f"{minute:02}")
        return result

s = Solution()
print(s.readBinaryWatch(1))
