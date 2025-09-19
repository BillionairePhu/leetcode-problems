class Spreadsheet:

  def __init__(self, rows: int):
    self.cols = {chr(i): {} for i in range(ord("A"), ord("Z") + 1)}
    
  def readCellPosition(self, cell:str) -> tuple[str, int]:
    return cell[0], int(cell[1:])

  def setCell(self, cell: str, value: int) -> None:
    col, row =  self.readCellPosition(cell)
    self.cols[col][row] = value

  def resetCell(self, cell: str) -> None:
    col, row =  self.readCellPosition(cell)
    if (row in self.cols[col]):
        self.cols[col].pop(row)

  def getValue(self, formula: str) -> int:
    op1, op2 = formula[1:].split('+')
    if (not op1.isnumeric()):
      col, row = self.readCellPosition(op1)
      op1 = self.cols[col][row] if row in self.cols[col] else 0
    else:
      op1 = int(op1)
    if (not op2.isnumeric()):
      col, row = self.readCellPosition(op2)
      op2 = self.cols[col][row] if row in self.cols[col] else 0
    else:
      op2 = int(op2)
    return op1 + op2