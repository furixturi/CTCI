# Validate BST: 
# Implement a function to check if a binary tree is a binary search
# tree.

from collections import deque

def validateBST(tree):
  q = deque()
  q.append(tree)
  while q:
    curr = q.popleft()
    if curr.left is not None and curr.left > curr:
      return False
    if curr.right is not None and curr.right < curr:
      return False
    if curr.left is not None:
      q.append(curr.left)
    if curr.right is not None:
      q.append(curr.right)
  return True