# First Common Ancestor: 
# Design an algorithm and write code to find the first common ancestor of 
# two nodes in a binary tree. Avoid storing additional nodes in a data 
# structure. NOTE: This is not necessarily a binary search tree.

def calcHeight(n):
  height = 0
  while n is not None:
    height += 1
    n = n.parent
  return height

def findCommonAncestor(n1, n2):
  if n1 == n2:
    return n1
  height1 = calcHeight(n1)
  height2 = calcHeight(n2)
  if height1 != height2:
    while height1 != height2:
      n1 = n1.parent
      height1 -=1
  else:
    while height1 != height2:
      n2 = n2.parent
      height2 -= 1
  while n1 != n2:
    n1 = n1.parent
    n2 = n2.parent
  return n1