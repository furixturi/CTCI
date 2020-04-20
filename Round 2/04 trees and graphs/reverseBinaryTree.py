# Note:
# Use recursion, start from the root
class Tree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __repr__(self):
    return str(self.value)

  def __str__(self, current=None, level=0, result=''):
    if level == 0:
      current = self
    else:
      result += '\n|' + (level-1) * ' |'
    valueStr = str(current.value) if current else '*'
    result += ('-' if level > 0 else '') + valueStr
    if current and (current.left or current.right):
      result = self.__str__(current.left, level+1, result)
      result = self.__str__(current.right, level+1, result)
    return result

# Modify orginal tree
def reverseTreeInPlace(tree):
  tmp = tree.left
  tree.left = tree.right
  tree.right = tmp
  if tree.left:
    reverseTreeInPlace(tree.left)
  if tree.right:
    reverseTreeInPlace(tree.right)

# Generate a new tree
def generateMirrorTree(oldCurr, newCurr=None, newTree=None):
  if not newTree:
    newCurr = Tree(oldCurr.value)
    newTree = newCurr
  if oldCurr.left:
    newCurr.right = Tree(oldCurr.left.value)
    newTree = generateMirrorTree(oldCurr.left, newCurr.right, newTree)
  if oldCurr.right:
    newCurr.left = Tree(oldCurr.right.value)
    newTree = generateMirrorTree(oldCurr.right, newCurr.left, newTree)
  return newTree

# Check two trees are mirroring each other
def isMirrorTrees(tr1, tr2):
  return tr1 is None and tr2 is None or (
      tr1 is not None and tr2 is not None and tr1.value == tr2.value
    ) and (
      isMirrorTrees(tr1.left, tr2.right) 
    ) and (
      isMirrorTrees(tr1.right, tr2.left)
    )

testTree = Tree(1)
testTree.left = Tree(2)
testTree.left.left = Tree(4)
testTree.left.right = Tree(5)
testTree.left.left.left = Tree(6)
testTree.right = Tree(3)
testTree.right.left = Tree(7)
testTree.right.left.right = Tree(8)

print(testTree, '\n=============')
reverseTreeInPlace(testTree)
print(testTree, '\n=============')
mirror = generateMirrorTree(testTree)
print(mirror, '\n=============')
print(isMirrorTrees(testTree, mirror))