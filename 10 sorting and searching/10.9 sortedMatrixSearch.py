# Sorted Matrix Search: Given an M x N matrix in which each row and each
# column is sorted in ascending order, write a method to find an
# element.

# O(M+N)
def findInMatrix(m, t):
  NUM_ROWS = len(m)
  NUM_COLS = len(m[0])
  r = 0
  c = NUM_COLS - 1
  n = None
  while r < NUM_ROWS and c >= 0:
    n = m[r][c]
    if n == t:
      return (r, c)
    if n < t:
      r += 1
    else:
      c -= 1
  return None

class Coordinate:
  def __init__(self, r = 0, c = 0):
    self.r = r
    self.c = c
  
  def isInbound(self, mtx):
    if len(mtx) == 0 or len(mtx[0]) == 0:
      return False
    return self.r < len(mtx) and self.c < len(mtx[0])

  def isBefore(self, c2):
    return self.r < c2.r and self.c < c2.c

def getDiagonalMid(s, e):
  if s.r == e.r and s.c == e.c:
    return s
  if not s.isBefore(e):
    raise ValueError('start point must be before end point and they can not be on the same row/column!')
  diagonalDist = min(e.r - s.r, e.c - s.c)
  return Coordinate(s.r + diagonalDist // 2, s.c + diagonalDist // 2)

def findInMatrixBinarySearch(mtx, t):
  return findInMatrixBSRecursive(mtx, t, Coordinate(0, 0), Coordinate(len(mtx)-1, len(mtx[0])-1))

# Pivot is at the coordinate where the number is either equals to t or
# the first greater than t
def findPivot(mtx, t, s, e):
  while s.isBefore(e):
    m = getDiagonalMid(s, e)
    if mtx[m.r][m.c] == t:
      return m
    if mtx[m.r][m.c] < t:
      s.r = m.r + 1
      s.c = m.c + 1
  if mtx[s.r][s.c] > t:
    return s
  else:
    return Coordinate(s.r+1, s.c+1)
  
def findInMatrixBSRecursive(mtx, t, s, e):
  if not s.isInbound(mtx) or not e.isInbound(mtx):
    return None
  if mtx[s.r][s.c] == t:
    return s
  p = findPivot(mtx, t, s, e)
  if mtx[p.r][p.c] == t:
    return p
  lowerLeftStart = Coordinate(p.r, s.c)
  lowerLeftEnd = Coordinate(e.r, p.c - 1)
  lowerLeftResult = findInMatrixBSRecursive(mtx, t, lowerLeftStart, lowerLeftEnd)
  if lowerLeftResult is None:
    upperRightStart = Coordinate(s.r, p.c)
    upperRightEnd = Coordinate(p.r - 1, e.c)
    return findInMatrixBSRecursive(mtx, t, upperRightStart, upperRightEnd)
  return lowerLeftResult