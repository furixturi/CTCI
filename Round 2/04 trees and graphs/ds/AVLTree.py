# Points to beware:
# 1. update height whenever you changed any node's left or right child
# 2. do not rebalance before updating height
# 3. when insert, assign the insert's return value to the tree reference
#   since it might be a different node that is now the root 
class AVLTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.height = 1

  def __repr__(self):
    return str(self.value)

  def insert(self, value, curr=None):
    if not curr:
      curr = self
    if value < curr.value:
      if not curr.left:
        curr.left = AVLTree(value)
      else:
        curr.left = self.insert(value, curr.left)
    elif value > curr.value:
      if not curr.right:
        curr.right = AVLTree(value)
      else:
        curr.right = self.insert(value, curr.right)
    else:
      print(f'{str(value)} already exists.')
    self.updateHeight(curr)
    curr = self.rebalance(curr)
    return curr
  
  def rebalance(self, node):
    leftH = node.left.height if node.left else 0
    rightH = node.right.height if node.right else 0
    # already balanced
    if abs(leftH - rightH) < 2:
      return node
    # left heavy
    if leftH > rightH:
      leftLeftH = node.left.left.height if node.left.left else 0
      leftRightH = node.left.right.height if node.left.right else 0
      # left right heavy
      if leftLeftH < leftRightH:
        node.left = self.rotateLeft(node.left)
      return self.rotateRight(node)
    # right heavy
    rightLeftH = node.right.left.height if node.right.left else 0
    rightRightH = node.right.right.height if node.right.right else 0
    # right left heavy
    if rightLeftH > rightRightH:
      node.right = self.rotateRight(node.right)
    return self.rotateLeft(node)

  def rotateLeft(self, node):
    newRoot = node.right
    node.right = newRoot.left
    self.updateHeight(node)
    newRoot.left = node
    self.updateHeight(newRoot)
    return newRoot

  def rotateRight(self, node):
    newRoot = node.left
    node.left = newRoot.right
    self.updateHeight(node)
    newRoot.right = node
    self.updateHeight(newRoot)
    return newRoot
    
  def updateHeight(self, node):
    leftH = node.left.height if node.left else 0
    rightH = node.right.height if node.right else 0
    node.height = max(leftH, rightH) + 1

if __name__ == '__main__':
  tr = AVLTree(1)
  tr = tr.insert(2)
  tr = tr.insert(3)
  tr = tr.insert(4)
  print(tr)