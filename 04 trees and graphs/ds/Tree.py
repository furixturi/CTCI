# The most generic tree
class Tree:
  def __init__(self, data):
    self.data = data
    self.children = []
  
  def add_child(self, data):
    child = Tree(data)
    self.children.append(child)

  def __repr__(self, level = 0):
    prefix = ('   ' * (level - 1) if level > 0 else '') + ('|--' if level > 0 else '')
    print_str = prefix + repr(self.data) + '\n'
    for child in self.children:
      print_str += child.__repr__(level + 1)
    return print_str


if __name__ == '__main__':
  tree = Tree(0)
  tree.add_child(1)
  tree.add_child(2)
  tree.add_child(3)
  tree.add_child(4)
  first_child = tree.children[0]
  first_child.add_child(5)
  first_child.add_child(6)
  first_child.add_child(7)
  first_child.add_child(8)
  second_child = tree.children[1]
  second_child.add_child(9)
  second_child.add_child(10)
  print(tree)