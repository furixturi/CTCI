# Check Balanced:
# Implement a function to check if a binary tree is balanced. 
# For the purposes of this question, a balanced tree is defined to be a tree such 
# that the heights of the two subtrees of any node never differ by more
# than one.

class BinaryTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def addHeight(tree):
  if tree.left is None and tree.right is None:
    tree.height = 1
  else:
    if tree.left is not None:
      tree.left = addHeight(tree.left)
    if tree.right is not None:
      tree.right = addHeight(tree.right)
    leftHeight = 0 if tree.left is None else tree.left.height
    rightHeight = 0 if tree.right is None else tree.right.height
    tree.height = max(leftHeight, rightHeight) + 1
  return tree

def isBalanced(tree):
  tree = addHeight(tree)
  nodes = [tree]
  while len(nodes) > 0:
    node = nodes.pop(0)
    if node.left:
      nodes.append(node.left)
    if node.right:
      nodes.append(node.right)
    leftHeight = 0 if node.left is None else node.left.height
    rightHeight = 0 if node.right is None else node.right.height
    if leftHeight - rightHeight < -1 or leftHeight - rightHeight > 1:
      return False
  return True

