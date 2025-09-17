from typing import List
from heapq import heapify, heappush, heappop

class FoodRatings:

  def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    self.foods_dict: dict[str, list] = {}
    self.cuisines_dict: dict[str, list] = {}
    
    for i in range(len(foods)):
      food, cuisine, rating = foods[i], cuisines[i], ratings[i]
      self.foods_dict[food] = [-rating, cuisine]
      if (cuisine in self.cuisines_dict):
        heappush(self.cuisines_dict[cuisine], (-rating, food))
      else:
        self.cuisines_dict[cuisine] = [(-rating, food)]

  def changeRating(self, food: str, newRating: int) -> None:
    cuisine = self.foods_dict[food][1]
    heappush(self.cuisines_dict[cuisine], (-newRating, food))
    self.foods_dict[food][0] = -newRating

  def highestRated(self, cuisine: str) -> str:
    while True:
      rating, food = heappop(self.cuisines_dict[cuisine])
      if (self.foods_dict[food][0] == rating):
        heappush(self.cuisines_dict[cuisine], (rating, food))
        return food


# Your FoodRatings object will be instantiated and called as such:
obj = FoodRatings(
  ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
  ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
  [9, 12, 8, 15, 14, 7]
)
print(obj.highestRated("korean"))
# print(obj.highestRated("japanese"))
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)