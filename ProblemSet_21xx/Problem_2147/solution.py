class Solution:
  def numberOfWays(self, corridor: str) -> int:
    result = 1
    curr_options, curr_chairs = 1, 0
    for object in corridor:
      if (object == "S"):
        if (curr_chairs < 2):
          curr_chairs += 1
        else:
          result = (result * curr_options) % (10**9 + 7)
          curr_options = 1
          curr_chairs = 1
      else:
        if (curr_chairs == 2):
          curr_options += 1
    # print(curr_options, curr_chairs)
    if (curr_chairs == 1 or curr_chairs == 0):
      return 0
    return result
        
s = Solution()
# print("Result", s.numberOfWays("SSPPSPS"))
# print("Result", s.numberOfWays("PPSPSP"))
# print("Result", s.numberOfWays("PPSPSPSSPPPSS"))
print("Result", s.numberOfWays("SPPSSSSPPS"))