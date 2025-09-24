class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    version1 = list(map(int, version1.split('.')))
    version2 = list(map(int, version2.split('.')))
    index = 0
    
    while index < max(len(version1), len(version2)):
      segment1 = version1[index] if index < len(version1) else 0
      segment2 = version2[index] if index < len(version2) else 0
      
      if (segment1 == segment2):
        index += 1
      elif (segment1 > segment2):
        return 1
      else:
        return -1
    return 0
    
s = Solution()
print(s.compareVersion("1.2", "2.0"))