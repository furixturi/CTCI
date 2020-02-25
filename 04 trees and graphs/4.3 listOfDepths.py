# List of Depths: 
# Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D
# linked lists).

class LinkedList:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    return str(self)

  def __str__(self):
    result = []
    curr = self
    while curr is not None:
      result.append(str(curr.data))
      curr = curr.next
    return ' -> '.join(result)

  def append(self, data):
    curr = self
    while curr.next is not None:
      curr = curr.next
    curr.next = LinkedList(data)

class BinaryTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
  def __repr__(self):
    return repr(self.data)
  
  
def listOfDepth(tree, level = 0, lists = []):
  if len(lists) - 1 < level:
    newLinkedList = LinkedList(tree.data)
    lists.append(newLinkedList)
  else:
    lists[level].append(tree.data)
  if tree.left is not None:
    listOfDepth(tree.left, level + 1, lists)
  if tree.right is not None:
    listOfDepth(tree.right, level + 1, lists) 
  return lists

tree = BinaryTree(5)
tree.left = BinaryTree(1)
tree.right = BinaryTree(8)
tree.left.left = BinaryTree(0)
tree.left.right = BinaryTree(2)
tree.right.left = BinaryTree(7)
tree.right.right = BinaryTree(9)

l = listOfDepth(tree)
print(l)

# ll = LinkedList(1)
# ll.append(2)
# ll.append(3)
# print(ll)