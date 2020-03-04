# Random Node: 
# You are implementing a binary search tree class from scratch which, in addition 
# to insert, find, and delete, has a method getRandomNode() which returns 
# a random node from the tree. All nodes should be equally likely to be chosen. 
# Design and implement an algorithm for getRandomNode, and explain how you 
# would implement the rest of the methods.
from random import randrange
class BST:
  def __init__(self, data):
    self.data = data
    self.size = 1
    self.left = None
    self.right = None
    self.parent = None

  def insert(self, data):
    if data == self.data:
      print(f'{data} already exists in the BST')
      return
    
    if data < self.data:
      if self.left is None:
        node = BST(data)
        self.left = node
        node.parent = self
      else:
        self.left.insert(data)
    else:
      if self.right is None:
        node = BST(data)
        self.right = node
        node.parent = self
      else:
        self.right.insert(data)
    self.size += 1

  def getRandomNode(self, randIdx = None):
    if self.size == 1:
      return self
    randIdx = randrange(self.size) if randIdx is None else randIdx
    leftSize = 0 if self.left is None else self.left.size
    if randIdx == leftSize:
      return self
    elif randIdx < leftSize:
      return self.left.getRandomNode(randIdx)
    else:
      return self.right.getRandomNode(randIdx - leftSize - 1)

  def delete(self, data):
    if data == self.data:
      if self.parent is not None:
        self.parent.size -= 1
        if self == self.parent.left:
          self.parent.left = None
        else:
          self.parent.right = None
        self.parent = None
      return self
    elif data < self.data:
      if self.left is None:
        print(f'{data} is not found in the BST')
        return None
      else:
        return self.left.delete(data)
    else:
      if self.right is None:
        print(f'{data} is not found in the BST')
        return None
      else:
        return self.right.delete(data)