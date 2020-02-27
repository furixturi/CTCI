# Successor: 
# Write an algorithm to find the "next" node (i.e., in-order successor) of 
# a given node in a binary search tree. You may assume that each node has 
# a link to its parent.

def findMin(tree):
  curr = tree
  while curr.left is not None:
    curr = curr.left
  return curr

def findNext(tree):
  curr = tree
  if curr == curr.parent.left:
    if curr.right is not None:
      nextNode = findMin(curr.right)
    else:
      nextNode = curr.parent
  else:
    if curr.right is not None:
      nextNode = findMin(curr.right)
    else:
      nextNode = None
  return nextNode