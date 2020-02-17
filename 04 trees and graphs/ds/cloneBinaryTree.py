from binaryTree import BinaryTree, printBinaryTree
# pre-order can be used to cloned a tree
def cloneBinaryTree(tree: BinaryTree) -> BinaryTree:
  if tree == None:
    return None
  n = BinaryTree(tree.data)
  if tree.left != None:
    n.left = cloneBinaryTree(tree.left)
  if tree.right != None:
    n.right = cloneBinaryTree(tree.right)
  return n

if __name__ == '__main__':
  tree = BinaryTree(1)
  tree.insert(2)
  tree.insert(3)
  tree.insert(4)
  tree.insert(5)
  tree.insert(6)
  tree.insert(7)
  tree.insert(8)
  print('original tree')
  printBinaryTree(tree)
  tree_clone = cloneBinaryTree(tree)
  print('cloned tree')
  printBinaryTree(tree_clone)