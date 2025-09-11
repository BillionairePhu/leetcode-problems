from typing import List


class Solution:
  def minimumTeachings(self,
    n: int, languages: List[List[int]], friendships: List[List[int]]
  ) -> int:
    languages_set = [set(language) for language in languages]
    result = len(languages)
    for i in range(1, n+1):
      learners = set()
      for friend1, friend2 in friendships:
        common_language = languages_set[friend1-1] & languages_set[friend2-1]
        # print(common_language)
        if (len(common_language) == 0):
          if ((friend1-1) not in learners and i not in languages_set[friend1-1]):
            learners.add(friend1-1)
          if ((friend2-1) not in learners and i not in languages_set[friend2-1]):
            learners.add(friend2-1)
      # print(i, learners)
      result = min(result, len(learners))
    return result          
  
s = Solution()
# print(s.minimumTeachings(11,
#     [[3,11,5,10,1,4,9,7,2,8,6],[5,10,6,4,8,7],[6,11,7,9],[11,10,4],[6,2,8,4,3],[9,2,8,4,6,1,5,7,3,10],[7,5,11,1,3,4],[3,4,11,10,6,2,1,7,5,8,9],[8,6,10,2,3,1,11,5],[5,11,6,4,2]],
#     [[7,9],[3,7],[3,4],[2,9],[1,8],[5,9],[8,9],[6,9],[3,5],[4,5],[4,9],[3,6],[1,7],[1,3],[2,8],[2,6],[5,7],[4,6],[5,8],[5,6],[2,7],[4,8],[3,8],[6,8],[2,5],[1,4],[1,9],[1,6],[6,7]]
#   ))
print(s.minimumTeachings(11, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]))