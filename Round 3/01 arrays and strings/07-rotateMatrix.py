# Rotate Matrix: Given an image represented by an NxN matrix, where each
# pixel in the image is 4 bytes, write a method to rotate the image by
# 90 degrees. Can you do this in place?
def rotateMatrix(m):
  for cycle in range(len(m)//2):
    idx_max = len(m) - 1 - cycle
    for j in range(cycle, idx_max):
      tmp = m[cycle][j]
      m[cycle][j] = m[idx_max-(j-cycle)][cycle]
      m[idx_max-(j-cycle)][cycle] = m[idx_max][idx_max-(j-cycle)]
      m[idx_max][idx_max-(j-cycle)] = m[j][idx_max]
      m[j][idx_max] = tmp

def printMatrix(m):
  for row in m:
    print(*row, sep='\t')

if __name__ == '__main__':
  print('======= m1 =======')
  m = [[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]
  printMatrix(m)
  print('============')
  rotateMatrix(m)
  printMatrix(m)
  print('======= m2 =======')
  m2 = [[1,2,3,4],
     [5, 6,7,8,],
     [9,10,11,12],
     [13,14,15,16]]
  printMatrix(m2)
  print('============')
  rotateMatrix(m2)
  printMatrix(m2)
  print('======= m3 =======')
  m3 = [[1,2,3],
     [4,5,6],
     [7,8,9]]
  printMatrix(m3)
  print('============')
  rotateMatrix(m3)
  printMatrix(m3)
  print('======= m4 =======')
  m4 = [[1]]
  printMatrix(m4)
  print('============')
  rotateMatrix(m4)
  printMatrix(m4)