from typing import List

class Solution:
  def solveSudoku(self, board: List[List[str]]) -> list[list[str]]:
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    sqr = [set() for _ in range(9)]
    
    for i in range(9):
      for j in range(9):
        if board[i][j] != ".":
          val = board[i][j]
          row[i].add(val)
          col[j].add(val)
          sqr[(i // 3) * 3 + (j // 3)].add(val)
          
    def isValueNotValid(val, i, j):
      return (val in row[i]) or (val in col[j]) or (val in sqr[(i//3)*3 + (j//3)])
    
    def fill(i: int, j: int) -> bool:
      if board[i][j] != ".":
        if i == 8 and j == 8:
          return True
        elif j == 8:
          return fill(i+1, 0)
        else:
          return fill(i, j+1)

      possible_values = [str(x) for x in range(1, 10)]

      for poss_val in possible_values:
        if (isValueNotValid(poss_val, i, j)):
          continue
        board[i][j] = poss_val
        row[i].add(poss_val)
        col[j].add(poss_val)
        sqr[(i//3)*3 + (j//3)].add(poss_val)
        
        if (i == 8 and j == 8):
          return True
        elif (j == 8):
          if fill(i+1, 0):
            return True
        else:
          if fill(i, j+1):
            return True
        
        row[i].remove(poss_val)
        col[j].remove(poss_val)
        sqr[(i//3)*3 + (j//3)].remove(poss_val)
        board[i][j] = "."
      return False
    fill (0, 0)

s = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
s.solveSudoku(board)

for row in board:
  print(row)
