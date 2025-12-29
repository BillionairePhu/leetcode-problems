from math import inf, sqrt
from typing import Counter, List
from fractions import Fraction


class Solution:
  def distance(self, point_a: list[int], point_b: list[int]):
    # keep your original function, but we won't use its float result as dict key
    return sqrt((point_a[0]-point_b[0])**2 + (point_a[1] - point_b[1])**2)
  
  def countTrapezoids(self, points: List[List[int]]) -> int:
    angles = {}
    for i in range(len(points)):
      point_a = points[i]
      for j in range(i+1, len(points)):
        point_b = points[j]

        x, y = point_b[0] - point_a[0], point_b[1] - point_a[1]

        # ✔ FIX 1: Rational slope (exact)
        angle = Fraction(y, x) if x != 0 else inf
        
        if angle not in angles:
          angles[angle] = {"roots": Counter(), "distances": {}, "edges": 0}
        
        # ✔ FIX 2: Rational root (line intercept)
        if angle != inf:
          root = Fraction(point_a[1], 1) - angle * Fraction(point_a[0], 1)
        else:
          root = Fraction(point_a[0], 1)

        angles[angle]["roots"][root] += 1
        angles[angle]["edges"] += 1

        # ✔ FIX 3: Use squared distance (rational) instead of float sqrt
        dx = x
        dy = y
        curr_distance = Fraction(dx*dx + dy*dy, 1)

        if curr_distance not in angles[angle]["distances"]:
          angles[angle]["distances"][curr_distance] = Counter()
        angles[angle]["distances"][curr_distance][root] += 1 
    
    result, parallelograms = 0, 0

    for angle in angles:
      curr_angle = angles[angle]
      sum_edges = curr_angle["edges"]
      all_roots = curr_angle["roots"]
      all_distances = curr_angle["distances"]
      
      if len(all_roots) < 2:
        continue
      
      # trapezoids
      for root in all_roots:
        result += all_roots[root] * (sum_edges - all_roots[root])
      
      # parallelograms
      for distance in all_distances:
        if len(all_distances[distance]) < 2:
          continue
        curr_distance_group = all_distances[distance]
        total = sum(curr_distance_group.values())
        for root in curr_distance_group:
          parallelograms += curr_distance_group[root] * (total - curr_distance_group[root])
        
    result = result // 2
    parallelograms = parallelograms // 4
    
    return result - parallelograms
