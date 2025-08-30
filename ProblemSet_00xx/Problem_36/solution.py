from typing import List


class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    sqr = [set() for _ in range(9)]
    
    for i in range(9):
      for j in range(9):
        if (board[i][j] == '.'):
          continue
        elif(board[i][j] in row[i] or board[i][j] in col[j] 
             or board[i][j] in sqr[(i//3)*3 + (j//3)]):
          return False
        else:
          row[i].add(board[i][j])
          col[j].add(board[i][j])
          sqr[(i//3)*3 + (j//3)].add(board[i][j])
    return True

# # Write your solution here
# from typing import List


# class Solution:
#   def isValidSudoku(self, board: List[List[str]]) -> bool:
#     row = [set() for _ in range(9)]
#     col = [set() for _ in range(9)]
#     sqr = [set() for _ in range(9)]
    
#     for i in range(9):
#       for j in range(9):
#         if (board[i][j] != '.'):
#           row[i].add(board[i][j])
#           col[j].add(board[i][j])
#           sqr[(i//3)*3 + (j//3)].add(board[i][j])
          
#     def isValueNotValid(val, i, j):
#       return (val in row[i]) or \
#         (val in col[j]) or (val in sqr[(i//3)*3 + (j//3)])
    
#     result = board.copy()
    
#     def fill(i: int, j: int):
#       possible_values = [board[i][j]] if board[i][j] != '.' \
#         else list(range(1, 10))
#       for poss_val in possible_values:
#         if (isValueNotValid(poss_val, i, j)):
#           continue
#         result[i][j] = str(poss_val)
#         row[i].add(str(poss_val))
#         col[j].add(str(poss_val))
#         sqr[(i//3)*3 + (j//3)].add(str(poss_val))
        
#         if (i == 8 and j == 8):
#           return
#         elif (j == 8):
#           fill(i+1, 0)
#         else:
#           fill(i, j+1)
          
#         if (result[8][8] != '.'):
#           return
        
#         row[i].remove(str(poss_val))
#         col[j].remove(str(poss_val))
    
#     fill (0, 0)
    
#     return result
  
# s = Solution()
# sudoku = s.isValidSudoku