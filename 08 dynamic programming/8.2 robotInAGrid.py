# Robot in a Grid: Imagine a robot sitting on the upper left corner of 
# grid with r rows and c columns. The robot can only move in two directions, 
# right and down, but certain cells are "off limits" such that the robot 
# cannot step on them. Design an algorithm to find a path for the robot from 
# the top left to the bottom right.
# Hints: #331, #360, #388

from random import randrange

class Tile:
  def __init__(self, x, y, isOffLimit = False):
    self.x = x
    self.y = y
    self.isOffLimit = isOffLimit
    self.right = None
    self.down = None

  def __repr__(self):
    return f'({self.x}, {self.y}) {self.isOffLimit}'

def buildGrid(r, c):
  grid = []
  for i in range(c):
    for j in range(r):
      isOffLimit = randrange(100) < 10
      if i == 0 and j == 0 or (i == c-1 and j == r-1):
        isOffLimit = False
      tile = Tile(i, j, isOffLimit)
      grid.append(tile)
  for k in range(len(grid)):
    tile = grid[k]
    if tile.y < r - 1:
      tile.down = grid[k + 1]
    if tile.x < c - 1:
      tile.right = grid[k + r]
  return grid

def findPath(grid):
  start = grid[0]
  goal = grid[len(grid) - 1]
  pathsToCheck = [[start]]
  while pathsToCheck:
    path = pathsToCheck.pop(0)
    lastTile = path[len(path) - 1]
    if lastTile.right is not None and not lastTile.right.isOffLimit:
      pathToRight = path + [lastTile.right]
      if lastTile.right == goal:
        return pathToRight
      else:
        pathsToCheck.append(pathToRight)
    if lastTile.down is not None and not lastTile.down.isOffLimit:
      pathToDown = path + [lastTile.down]
      if lastTile.down == goal:
        return pathToDown
      else:
        pathsToCheck.append(pathToDown)
  return None

if __name__ == '__main__':
  grid = buildGrid(3, 5)
  findPath(grid)