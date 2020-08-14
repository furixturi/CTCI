# Zero Matrix: Write an algorithm such that if an element in an MxN
# matrix is 0, its entire row and column are set to 0.


def zeroMatrix(m):
    M = len(m)
    N = len(m[0])
    rz = set()
    cz = set()
    for i in range(M):
        for j in range(N):
            if m[i][j] == 0:
                rz.add(i)
                cz.add(j)
    for r in rz:
        m[r] = [0] * N
    for c in cz:
        for r in range(M):
            m[r][c] = 0


def printMatrix(matrix):
    for row in matrix:
        print(*row, sep='\t')


if __name__ == '__main__':
  test_matrix = [
      [0, 1, 2, 4, 5],
      [3, 0, 1, 6, 7],
      [2, 4, 5, 3, 9]
  ]
  printMatrix(test_matrix)
  zeroMatrix(test_matrix)
  print('=== zero out ===')
  printMatrix(test_matrix)
