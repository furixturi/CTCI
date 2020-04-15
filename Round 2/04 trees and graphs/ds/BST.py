from collections import deque
class BST:
  def __init__(self, rootVal):
    self.data = rootVal
    self.left = None
    self.right = None
    self.parent = None
    self.count = 1

  def __repr__(self):
    return str(self.data)

  def insert(self, val, currentNode = None):
    if not currentNode:
      currentNode = self
    if val == currentNode.data:
      currentNode.count += 1
    elif val < currentNode.data:
      if not currentNode.left:
        n = BST(val)
        n.parent = currentNode
        currentNode.left = n
      else:
        self.insert(val, currentNode.left)
    else:
      if not currentNode.right:
        n = BST(val)
        n.parent = currentNode
        currentNode.right = n
      else:
        self.insert(val, currentNode.right)

  def findNode(self, val, currentNode = None):
    if not currentNode:
      currentNode = self
    if currentNode.data == val:
      return currentNode
    if val < currentNode.data:
      return self.findNode(val, currentNode.left) if currentNode.left else None
    else:
      return self.findNode(val, currentNode.right) if currentNode.right else None
      
  def findMin(self, currentNode = None):
    if not currentNode:
       currentNode = self
    if not currentNode.left:
      return currentNode
    return self.findMin(currentNode.left)
  
  def delete(self, data):
    n = self.findNode(data)
    if n:
      if n.count > 1:
        n.count -= 1
        return
      if n.right:
        nextBigger = n.right.findMin()
        n.data = nextBigger.data
        nextBigger.parent.left = nextBigger.right
        return self
      if n.parent:
        if n == n.parent.left:
          n.parent.left = n.left
        else:
          n.parent.right = n.left
        return self
      n.left.parent = None
      return n.left
    else:
      print(f'{data} not found.')
      return self

  def dfsPreOrder(self, traverseFunc, currentNode=None):
    if not currentNode:
      currentNode = self
    traverseFunc(currentNode)
    if currentNode.left:
      self.dfsPreOrder(traverseFunc, currentNode.left)
    if currentNode.right:
      self.dfsPreOrder(traverseFunc, currentNode.right)
  
  def dfsInOrder(self, traverseFunc, currentNode=None):
    if not currentNode:
      currentNode = self
    if currentNode.left:
      self.dfsInOrder(traverseFunc, currentNode.left)
    traverseFunc(currentNode)
    if currentNode.right:
      self.dfsInOrder(traverseFunc, currentNode.right)
  
  def dfsPostOrder(self, traverseFunc, currentNode=None):
    if not currentNode:
      currentNode = self
    if currentNode.left:
      self.dfsPostOrder(traverseFunc, currentNode.left)
    if currentNode.right:
      self.dfsPostOrder(traverseFunc, currentNode.right)
    traverseFunc(currentNode)

  def bfs(self, traverseFunc):
    q = deque([self])
    while q:
      currentNode = q.popleft()
      if currentNode.left:
        q.append(currentNode.left)
      if currentNode.right:
        q.append(currentNode.right)
      traverseFunc(currentNode)

def findNextBigger(tree):
  if tree.right:
    return tree.right.findMin()
  if tree.parent and tree == tree.parent.left:
    return tree.parent
  return None

if __name__ == "__main__":
  tr = BST(4)
  tr.insert(2)
  tr.insert(3)
  tr.insert(1)
  tr.insert(5)
  subtree = tr.findNode(2)
  # print(subtree)
  mintree = tr.right.findMin()
  # print(mintree)
  print('=== Pre Order ===')
  tr.dfsPreOrder(lambda n:print(n))
  print('=== In Order ===')
  tr.dfsInOrder(lambda n:print(n))
  print('=== Post Order ===')
  tr.dfsPostOrder(lambda n:print(n))
  print('=== BFS ===')
  tr.bfs(lambda n:print(n))