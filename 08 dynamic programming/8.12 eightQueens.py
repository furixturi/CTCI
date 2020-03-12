# Eight Queens: Write an algorithm to print all ways of arranging eight
# queens on an 8x8 chess board so that none of them share the same row,
# column, or diagonal. In this case, "diagonal" means all diagonals, not
# just the two that bisect the board.
NUM_ROW = 8
NUM_COL = 8


def placeQueen(r, lastBoard, results):
  if r == NUM_ROW:
    results.append(lastBoard)
  else:
    for c in range(NUM_COL):
      if placable(r, c, lastBoard):
        newBoard = lastBoard[:]
        newBoard[r] = c
        placeQueen(r + 1, newBoard, results)

def placable(r, c, currentBoard):
  for row in range(r):
    col = currentBoard[row]
    if col == c or abs(row - r) == abs(col -c):
      return False
  return True


results = []
placeQueen(0, [-1] * NUM_ROW, results)
print(results)