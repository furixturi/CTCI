class AVLTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.height = 1

  def __repr__(self) -> str:
    return repr(self.data)

  def __str__(self, level=0) -> str:
    prefix = '' if level == 0 else '         ' * (level - 1)
    prefix += '' if level == 0 else '|-- '
    data_str = '*' if self == None else f'{repr(self)} (h: {str(self.height)})'
    result_str = prefix + data_str + '\n'
    if self != None and (self.left != None or self.right != None):
      result_str += AVLTree.__str__(self.left, level + 1)
      result_str += AVLTree.__str__(self.right, level + 1)
    return result_str

  def insert(self, data, parent=None, is_root=True):
    if is_root == True:
      parent = self
    # BST recursive insert and update parent height
    if parent == None:
      return AVLTree(data)
    if data == parent.data:
      raise ValueError(f'{data} already exists.')
    if data < parent.data:
      parent.left = self.insert(data, parent.left, False)
    else:
      parent.right = self.insert(data, parent.right, False)
    parent.height = max(self.get_height(parent.left),
                      self.get_height(parent.right)) + 1
    # rebalance
    balance = self.get_balance(parent)
    # left heavy
    if balance > 1:
      balance_child = self.get_balance(parent.left)
      # left left
      if balance_child > 0:
        parent = self.rotate_right(parent)
      # left right
      else:
        parent.left = self.rotate_left(parent.left)
        parent = self.rotate_right(parent)
    # right heavy
    elif balance < -1:
      balance_child = self.get_balance(parent.right)
      # right right
      if balance_child < 0:
        parent = self.rotate_left(parent)
      # right left
      else:
        parent.right = self.rotate_right(parent.right)
        parent = self.rotate_left(parent)
    return parent

  def rotate_right(self, old_parent):
    new_parent = old_parent.left
    old_parent.left = new_parent.right
    new_parent.right = old_parent
    old_parent.height = max(self.get_height(
      old_parent.left), self.get_height(old_parent.right)) + 1
    new_parent.height = max(self.get_height(
      new_parent.left), self.get_height(new_parent.right)) + 1
    return new_parent

  def rotate_left(self, old_parent):
    new_parent = old_parent.right
    old_parent.right = new_parent.left
    new_parent.left = old_parent
    old_parent.height = max(self.get_height(
      old_parent.left), self.get_height(old_parent.right)) + 1
    new_parent.height = max(self.get_height(
      new_parent.left), self.get_height(new_parent.right)) + 1
    return new_parent

  def get_height(self, node):
    if node == None:
      return 0
    else:
      return node.height

  def get_balance(self, node):
    if not node:
      return 0
    return self.get_height(node.left) - self.get_height(node.right)


if __name__ == '__main__':
  tree = AVLTree(5)
  tree.insert(2)
  tree.insert(9)
  tree.insert(3)
  tree.insert(4)
  tree.insert(12)
  tree.insert(10)
  tree.insert(13)
  print(tree)
