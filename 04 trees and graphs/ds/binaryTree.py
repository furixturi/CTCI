import random

class BinaryTree:
  def __init__(self, data):
    self.values = set()
    self.values.add(data)
    self.data = data
    self.left = None
    self.right = None

  def __repr__(self) -> str:
    return repr(self.data)
  
  def __str__(self, level=0) -> str:
    if self == None:
      return ''
    prefix = '' if level == 0 else '   ' * (level - 1)
    prefix += '' if level == 0 else '|--'
    result_str = prefix + str(self.data)
    if self.left != None:
      result_str += self.left.__str__(level + 1)
    if self.right != None:
      result_str += self.right.__str__(level + 1)
    return result_str


  def insert(self, data, values = None):
    if values != None:
      values.update(self.values)
    if values != None and data in values:
      raise ValueError('{data} already exists.')
    if self.left != None and self.right != None:
      r = random.randrange(2)
      if r == 0:
        self.left.insert(data, values)
      else:
        self.right.insert(data, values)
    else:
      t = self
      n = BinaryTree(data)
      if t.left == None:
        t.left = n
      elif t.right == None:
        t.right = n
      else:
        r = random.randrange(2)
        if r == 0:
          t.left = n
        else:
          t.right = n
      self.values.add(data)

def printBinaryTree(t: BinaryTree, level=0):
  if t == None:
    return
  prefix = '   ' * (level - 1) if level > 0 else ''
  prefix += '|--' if level > 0 else ''
  print(prefix + str(t.data))
  if t.left != None:
    printBinaryTree(t.left, level + 1)
  if t.right != None:
    printBinaryTree(t.right, level + 1)