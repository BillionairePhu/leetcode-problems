class Solution:
  def countCollisions(self, directions: str) -> int:
    cars_moving_right, obstacle_on_left = 0, False
    collisions = 0
    
    for direction in directions:
      if (direction == "R"):
        cars_moving_right += 1
        obstacle_on_left = True
      elif (direction == "S"):
        collisions += cars_moving_right
        cars_moving_right = 0
        obstacle_on_left = True
      else:
        if (obstacle_on_left == True):
          collisions += (cars_moving_right + 1)
          cars_moving_right = 0
    return collisions