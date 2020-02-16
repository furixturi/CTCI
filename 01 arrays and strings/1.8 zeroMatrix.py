# Zero Matrix: 
# Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.

# Time complexity O(M*N)
# Space complexity O(max(M, N))
from typing import List
Matrix = List[List[int]]

def zeroMatrix(matrix: Matrix):
  N = len(matrix)    # number of rows
  M = len(matrix[0]) # number of columns
  rows_zero = []
  columns_zero = []
  for n in range(N):
    for m in range(M):
      if matrix[n][m] == 0:
        rows_zero.append(n)
        columns_zero.append(m)
  for row in rows_zero:
    matrix[row] = [0] * M
  for column in columns_zero:
    for n in range(N):
      matrix[n][column] = 0

def printMatrix(matrix: Matrix):
  for row in matrix:
    print(*row, sep='\t')

test_matrix = [
  [0, 1, 2, 4, 5],
  [3, 0, 1, 6, 7],
  [2, 4, 5, 3, 9]
]

printMatrix(test_matrix)
zeroMatrix(test_matrix)
print('=== zero out ===')
printMatrix(test_matrix)