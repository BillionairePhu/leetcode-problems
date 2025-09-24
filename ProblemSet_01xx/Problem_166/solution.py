class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    sign = "-" if (numerator/denominator < 0) else ""
    
    numerator = abs(numerator)
    denominator = abs(denominator)

    encounterd = {}
    
    whole = numerator // denominator
    numerator = numerator % denominator
    numerator *= 10
    
    digits = []
    while True:
      if (numerator == 0 or numerator in encounterd):
        break
      
      encounterd[numerator] = len(digits)
      digit = numerator // denominator
      digits.append(digit)
      numerator = numerator % denominator
      numerator *= 10
    
    if (len(digits) == 0):
      return sign + str(whole)
    elif (numerator == 0):
      return sign + str(whole) + "." + "".join(map(str, digits))
    else:
      index = encounterd[numerator]
      result = sign + str(whole) + "." + "".join(map(str, digits[:index])) + "(" + "".join(map(str, digits[index:])) + ")"
      return result

s = Solution()
print(s.fractionToDecimal(-50, 8))
# print(s.fractionToDecimal(4, 333))
# print(s.fractionToDecimal(11, 2))