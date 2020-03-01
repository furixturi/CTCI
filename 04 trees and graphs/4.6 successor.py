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
  if curr.right is not None:
    nextNode = findMin(curr.right)
  else:
    if curr.parent is None:
      nextNode = None
    else:
      if curr == curr.parent.left:
        nextNode = curr.parent
      else:
        nextNode = None
        curr = curr.parent
        while curr.parent is not None:
          curr = curr.parent
          if curr == curr.parent.left:
            nextNode = curr.parent
            break
  return nextNode