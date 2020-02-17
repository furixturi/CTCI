from ds.binaryTree import BinaryTree, printBinaryTree

# pre-order can be used to flip a tree
def flipBinaryTree(t: BinaryTree):
  if t == None or (t.left == None and t.right == None):
    return
  t.left, t.right = t.right, t.left
  if t.left != None:
    flipBinaryTree(t.left)
  if t.right != None:
    flipBinaryTree(t.right)

def flipCopyBinaryTree(t: BinaryTree) -> BinaryTree:
  if t == None:
    return None
  if t.left == None and t.right == None:
    return BinaryTree(t.data)
  new_t = BinaryTree(t.data)
  if t.left != None:
    new_t.right = flipCopyBinaryTree(t.left)
  if t.right != None:
    new_t.left = flipCopyBinaryTree(t.right)
  return new_t  

if __name__ == '__main__':
  tree = BinaryTree(1)
  tree.insert(2)
  tree.insert(3)
  tree.insert(4)
  tree.insert(5)
  tree.insert(6)
  tree.insert(7)
  print('the tree')
  printBinaryTree(tree)
  # flipBinaryTree(tree)
  # print('the tree after flipped')
  # printBinaryTree(tree)
  flipCopy = flipCopyBinaryTree(tree)
  print('the flipped copy of the original tree')
  printBinaryTree(flipCopy)
  print('the original again, should not be changed')
  printBinaryTree(tree)
