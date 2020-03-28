# RankfromStream: Imagine you are reading in a stream of integers.
# Periodically, you wish to be able to look up the rank of a number x
# (the number of values less than or equal to x). 
# Implement the data structures and algorithms to support these operations. 
# That is, implement the method track(int x), which is called when each number 
# is generated, and the method getRankOfNumber(int x), which returns the number 
# of values less than or equal to x (not including x itself).
# EXAMPLE
# Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(1) = 0 
# getRankOfNumber(3) = 1 
# getRankOfNumber(4) = 3

nums = None

class BST:
  def __init__(self, data):
    self.data = data
    self.count = 1
    self.left = None
    self.right = None


  def __repr__(self, level=0):
    # if level == 0:
    #   print(f'parent: {repr(self.parent.data) if self.parent != None else repr(None)}')
    prefix = ('   ' * (level - 1) if level > 0 else '') + ('|--' if level > 0 else '')
    print_str = prefix + ('*' if self == None else repr(self.data) + '(' + repr(self.count) + ')') + '\n'
    if self != None and (self.left != None or self.right != None):
      print_str += BST.__repr__(self.left, (level + 1))
      print_str += BST.__repr__(self.right, (level + 1))
    return print_str

  def insert(self, data):
    current = self
    while True:
      if data == current.data:
        current.count += 1
        return
      if data > current.data:
        if current.right is None:
          current.right = BST(data)
          return
        else:
          current = current.right
      else:
        if current.left is None:
          current.left = BST(data)
          return
        else:
          current = current.left
  
  def inOrder(self, list):
    if self.left:
      BST.inOrder(self.left, list)
    i = self.count
    while i > 0:
      list.append(self.data)
      i -= 1
    if self.right:
      BST.inOrder(self.right, list)

def track(x):
  global nums
  if nums is None:
    nums = BST(x)
  else:
    nums.insert(x)

def getRankOfNumber(num):
  global nums
  sorted = []
  nums.inOrder(sorted)
  i = 0
  while i < len(sorted) and sorted[i] <= num:
    i += 1
  return i - 1

if __name__ == '__main__':
  print(f'nums: \n{nums}')
  track(26)
  track(17)
  track(99)
  track(2)
  track(99)
  print(f'nums: \n{nums}')
  print(getRankOfNumber(99))
  print(getRankOfNumber(2))
  print(getRankOfNumber(17))
  print(getRankOfNumber(26))


