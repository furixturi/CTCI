# Minimal Tree: 
# Given a sorted (increasing order) array with unique integer elements, 
# write an algo­rithm to create a binary search tree with minimal
# height.



class AVLTree:
  def __init__(self, data):
    if data == None:
      raise ValueError('Tree key cannot be None')
    self.data = data
    self.left = None
    self.right = None
    self.height = 1  

  def __repr__(self):
    return repr(self.data)  

  def updateHeight(self):
    if self.left == None and self.right == None:
      self.height = 1
    else:
      leftHeight = 0 if not self.left else self.left.height
      rightHeight = 0 if not self.right else self.right.height
      self.height = max(leftHeight, rightHeight) + 1

  def getBalance(self):
    leftHeight = 0 if not self.left else self.left.height
    rightHeight = 0 if not self.right else self.right.height
    return leftHeight - rightHeight

  def rotateRight(self):
    newRoot = self.left
    self.left = newRoot.right
    newRoot.right = self
    return newRoot

  def rotateLeft(self):
    newRoot = self.right
    self.right = newRoot.left
    newRoot.left = self
    return  newRoot

  def rebalance(self):
    # rebalance
    balance = self.getBalance()
    # left heavy
    if balance > 1:
      subBalance = self.left.getBalance()
      # left left
      if subBalance > 0:
        self = self.rotateRight()
      # left right
      else:
        self.left = self.left.rotateLeft()
        self = self.rotateRight
    # right heavy
    elif balance < -1:
      subBalance = self.right.getBalance()
      # right right
      if subBalance < 0:
        self = self.rotateLeft()
      # right left
      else:
        self.right = self.right.rotateRight()
        self = self.rotateLeft()
    return self

  def insert(self, data):
    if data < self.data:
      if self.left:
        self.left = self.left.insert(data)
      else:
        self.left = AVLTree(data)
    else:
      if self.right:
        self.right = self.right.insert(data)
      else:
        self.right = AVLTree(data)
    self.updateHeight()
    return self.rebalance()

    
def generateMinimalTree(list):
  tree = AVLTree(list[0])
  for n in list[1:]:
    tree = tree.insert(n)
  return tree

t = generateMinimalTree([5,8,2,9,7,1,0])
print(t)