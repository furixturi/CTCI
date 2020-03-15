# Sorted Merge: You are given two sorted arrays, A and B, where A has a
# large enough buffer at the end to hold B. Write a method to merge B
# into A in sorted order.

def mergeSorted(A, B):
  C = A[:len(A) - len(B)]
  b = 0
  c = 0
  a = 0
  while b < len(B) and c < len(C):
    if B[b] < C[c]:
      A[a] = B[b]
      b += 1
    else:
      A[a] = C[c]
      c += 1
    a += 1
  while b < len(B):
    A[a] = B[b]
    a += 1
    b += 1
  while c < len(C):
    A[a] = C[c]
    a += 1
    c += 1
def mergeSortedSolution(A, B):
  a = len(A) - len(B) - 1
  b = len(B) - 1
  i = len(A) - 1
  while b >= 0:
    if a >= 0 and A[a] > B[b]:
      A[i] = A[a]
      a -= 1
    else:
      A[i] = B[b]
      b -= 1
    i -= 1

A = [2, 5, 6, 7, 8, None, None, None, None]
B = [1, 3, 4, 9]
mergeSortedSolution(A, B)
print(A)