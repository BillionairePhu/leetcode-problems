from typing import List
from heapq import heappush, heappop, nsmallest


class MovieRentingSystem:

  def __init__(self, n: int, entries: List[List[int]]):
    # A min heap to store the rented movie
    # => keep track of cheapest rented movies for "report"
    self.rented = []
    # A dictionary to store a movie copy's information
    # The key is a tuple of shop and movie (identifying a movie copy)
    # The value is a list consisting of the copy's price and rental status (rented or not)
    self.copy_infos = {}
    # A dictionary to store a heap of copies for each movie
    # => keep track of cheaptest copies of each movie for "search"
    self.movies_dict = {}
    
    # Input entry information into "copy_infos" and "movies_dict"
    for entry in entries:
      shop, movie, price = entry
      
      self.copy_infos[(shop, movie)] = [price, False]
      
      if (movie not in self.movies_dict):
        self.movies_dict[movie] = [[price, shop]]
      else:
        heappush(self.movies_dict[movie], [price, shop])

  def search(self, movie: int) -> List[int]:
    if (movie not in self.movies_dict):
      return []
    movie_list = self.movies_dict[movie]
    index, result = 0, []
    result_set = set()
    # Popping 5 smallest unrent result from the movie heap
    while (index < 5 and len(movie_list) > 0):
      price, shop = heappop(movie_list)
      if (self.copy_infos[(shop, movie)][1] == False and shop not in result_set):
        result.append([shop, movie, price])
        index += 1
        result_set.add(shop)
    # Pushing these results pack
    for copy in result:
      heappush(movie_list, [copy[2], copy[0]])
    return [copy[0] for copy in result]

  def rent(self, shop: int, movie: int) -> None:
    # Set the rent flag at the copy info to True
    copy_info = self.copy_infos[(shop, movie)]
    copy_info[1] = True
    
    # Push it to the rented heap
    heappush(self.rented, [copy_info[0], shop, movie])

  def drop(self, shop: int, movie: int) -> None:
    # Set the rent flag at copy info to False
    copy_info = self.copy_infos[(shop, movie)]
    copy_info[1] = False
    
    # Push it to the movie heap
    heappush(self.movies_dict[movie], [copy_info[0], shop])

  def report(self) -> List[List[int]]:
    index, result = 0, []
    result_set = set()
    # Popping 5 smallest unrent result from the movie heap
    while (index < 5 and len(self.rented) > 0):
      price, shop, movie = heappop(self.rented)
      if (self.copy_infos[(shop, movie)][1] == True and (shop, movie) not in result_set):
        result.append([shop, movie, price])
        result_set.add((shop, movie))
        index += 1
    # Pushing these results pack
    for copy in result:
      heappush(self.rented, [copy[2], copy[0], copy[1]])
    return [copy[:2] for copy in result]


# Your MovieRentingSystem object will be instantiated and called as such:
obj = MovieRentingSystem(3, [[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]])
print(obj.search(1))
obj.rent(0,1)
obj.rent(1,2)
print(obj.report())
obj.drop(1,2)
print(obj.search(2))
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()