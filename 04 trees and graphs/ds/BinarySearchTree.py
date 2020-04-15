from __future__ import annotations
from typing import List
from Tree import Tree
from collections import deque
class BinarySearchTree(Tree):
  def __init__(self, data):
    self.data = data
    self.parent = None
    self.left_child = None
    self.right_child = None
  
  def __repr__(self, level=0):
    if level == 0:
      print(f'parent: {repr(self.parent.data) if self.parent != None else repr(None)}')
    prefix = ('   ' * (level - 1) if level > 0 else '') + ('|--' if level > 0 else '')
    print_str = prefix + ('*' if self == None else repr(self.data)) + '\n'
    if self != None and (self.left_child != None or self.right_child != None):
      print_str += BinarySearchTree.__repr__(self.left_child, (level + 1))
      print_str += BinarySearchTree.__repr__(self.right_child, (level + 1))
    return print_str

  # best case O(logN)
  # worst case O(N)
  def insert(self, data):
    child = BinarySearchTree(data)
    n = self
    while True:
      if data < n.data:
        if n.left_child == None:
          child.parent = n
          n.left_child = child
          return
        else:
          n = n.left_child
      elif data > n.data:
        if n.right_child == None:
          child.parent = n
          n.right_child = child
          return
        else:
          n = n.right_child
      else:
        raise ValueError(f'{data} is already in the BST. No duplicate data is allowed.')

  # best case O(logN)
  # worst case O(N)
  def search(self, data) -> BinarySearchTree:
    curr = self
    while True:
      if data == curr.data:
        break
      elif data > curr.data:
        if curr.right_child != None:
          curr = curr.right_child
        else:
          curr = None
          break
      else:
        if curr.left_child != None:
          curr = curr.left_child
        else:
          curr = None
          break
    return curr

  # best case O(logN)
  # worst case O(N)
  def search_min(self) -> BinarySearchTree:
    curr = self
    while curr.left_child != None:
      curr = curr.left_child
    return curr
    
  # best case O(logN)
  # worst case O(N)
  def delete(self, data):
    n = self.search(data)
    if n == None:
      raise ValueError(f'{data} is not in the tree. Cannot delete inexistent node.')
    else:
      if n.left_child == None and n.right_child == None:
        if n.data > n.parent.data:
          n.parent.right_child = None # What if n is the root?
        else:
          n.parent.left_child = None
      elif (n.left_child != None and n.right_child == None) or (n.left_child == None and n.right_child != None):
        child = n.left_child if n.left_child != None else n.right_child
        if n.data > n.parent.data:
          n.parent.right_child = child
        else:
          n.parent.left_child = child
      else:
        next_bigger = n.right_child.search_min()
        n.data = next_bigger.data
        if next_bigger.data > next_bigger.parent.data:
          next_bigger.parent.right_child = None # What about nextBigger's right child?
        else:
          next_bigger.parent.left_child = None
  # O(N)
  # get's sorted values
  def dfs_in_order(self, traverse_function):
    if self != None:
      left_child = self.left_child
      right_child = self.right_child
      # left_child might be None
      BinarySearchTree.dfs_in_order(left_child, traverse_function)
      traverse_function(self)
      # right_child might be None
      BinarySearchTree.dfs_in_order(right_child, traverse_function)
  
  # O(N)
  # can replicate a BST (if null leaves are identified)
  def dfs_pre_order(self, traverse_function):
    if self != None:
      left_child = self.left_child
      right_child = self.right_child
      traverse_function(self)
      BinarySearchTree.dfs_pre_order(left_child, traverse_function)
      BinarySearchTree.dfs_pre_order(right_child, traverse_function)
  
  # O(N)
  # can be used to delete a tree
  def dfs_post_order(self, traverse_function):
    if self != None:
      left_child = self.left_child
      right_child = self.right_child
      BinarySearchTree.dfs_post_order(left_child, traverse_function)
      BinarySearchTree.dfs_post_order(right_child, traverse_function)
      traverse_function(self)

  # O(N)
  # it is not a recursive function
  def bfs(self, traverse_function):
    queue: deque = deque()
    queue.append(self)
    while queue:
      n = queue.popleft()
      if n.left_child is not None:
        queue.append(n.left_child)
      if n.right_child is not None:
        queue.append(n.right_child)
      traverse_function(n)

def traverse_func(node: BinarySearchTree):
  print(repr(node.data), end=', ')

if __name__ == '__main__':
  bst = BinarySearchTree(5)
  bst.insert(3)
  bst.insert(1)
  bst.insert(2)
  bst.insert(4)
  bst.insert(7)
  bst.insert(8)
  bst.insert(6)
  # print(bst)
  # try:
  #   bst.insert(6)
  # except Exception as ex:
  #   print(f'!!{(type(ex).__name__).upper()}!! {ex.args[0]}')
  # print('In-Order')
  # bst.dfs_in_order(traverse_func)
  # print('\nPre-Order')
  # bst.dfs_pre_order(traverse_func)
  # print('\nPost-Order')
  # bst.dfs_post_order(traverse_func)
  # print('\nBread-First')
  # bst.bfs(traverse_func)
  # target = bst.search(3)
  # print(target)
  # print(bst.search_min())
  # bst.delete(10)
  # bst.delete(2)
  # bst.delete(5)
  bst.delete(1)
  print(bst)
