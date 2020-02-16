# Rotate Matrix: 
# Given an image represented by an NxN matrix, where each pixel in the image 
# is 4 bytes, write a method to rotate the image by 90 degrees. 
# Can you do this in place?
from typing import List
Matrix = List[List[int]]

# Time complexity O(N^2)
# Space complexity O(1)
def rotateMatrix(matrix: Matrix):
  ring = len(matrix)
  row = column = i = j = i0 = i1 = i2 = i3 = j0 = j1 = j2 = j3 = 0

  while ring >= 2:
    i = 0
    j = 0
    # print(f'ring: {ring} row: {row} column: {column} i: {i} j: {j}')
    while j <= ring -2:
      # print(f'>>> j: {j}')
      i0 = i + row
      j0 = j + column
      i1 = ring-1-j + row
      j1 = i + column
      i2 = ring-1-i + row
      j2 = ring-1-j + column
      i3 = j + row
      j3 = ring-1-i + column
      # print(f'    [{i0}][{j0}]: {matrix[i0][j0]} | [{i1}][{j1}]: {matrix[i1][j1]} | [{i2}][{j2}]: {matrix[i2][j2]} | [{i3}][{j3}]: {matrix[i3][j3]} ')
      matrix[i0][j0], matrix[i1][j1] = matrix[i1][j1], matrix[i0][j0]
      matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]
      matrix[i2][j2], matrix[i3][j3] = matrix[i3][j3], matrix[i2][j2]
      j += 1
    # print(f'after ring {ring}: {matrix}')
    ring -= 2
    row += 1
    column += 1

# Time complexity O(N^2)
# Space complexity O(1)
def rotateMatrixSolution(m: Matrix):
  N = len(m)
  for cycle in range(N // 2):
    first = cycle
    last = N - 1 - cycle
    for i in range(first, last):
      offset = i - first
      top = m[cycle][i]
      # put left to top
      m[first][i] = m[last-offset][first]
      # put bottom to right
      m[last-offset][first] = m[last][last-offset]
      # put right to bottom
      m[last][last-offset] = m[i][last]
      # put top to right
      m[i][last] = top

# m = [[1,2,3,4],
#       [5,6,7,8],
#       [9,10,11,12],
#       [13,14,15,16]]
def printMatrix(matrix: Matrix):
  for row in matrix:
    print(*row, sep='\t')

m = [[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]
printMatrix(m)
rotateMatrix(m)
# rotateMatrixSolution(m)
print('=========== ROTATE! ===========')
printMatrix(m)
rotateMatrixSolution(m)
print('=========== ROTATE AGAIN! ===========')
printMatrix(m)




