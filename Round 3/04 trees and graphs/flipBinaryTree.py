class BT:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def __repr__(self):
    return str(self.data)

  def __str__(self, level=0):
    prefix = '' if level == 0 else ('\n' + '  ' * (level-1) + '|-')
    if self == None:
      return prefix + 'None'
    res = prefix + str(self.data)
    if self.left != None or self.right != None:
      res += BT.__str__(self.left, level+1)
      res += BT.__str__(self.right, level+1)
    return res

def fbt(t):
  if t == None:
    return None
  t.left, t.right = fbt(t.right), fbt(t.left)
  return t

def cpt(t):
  if t == None:
    return None
  ct = BT(t.data)
  ct.left = cpt(t.left)
  ct.right = cpt(t.right)
  return ct

if __name__ == '__main__':
  t = BT(5)
  t.left = BT(2)
  t.right = BT(1)
  t.left.left = BT(3)
  t.left.right = BT(4)
  t.left.right.left = BT(7)
  t.right.right = BT(6)
  # print(t)
  # fbt(t)
  print('=== t ===')
  print(t)
  t2 = cpt(t)
  print('=== t2 ===')
  print(t2)
  fbt(t2)
  print('=== t after fbt(t2) ===')
  print(t)
  print('=== t2 after fbt(t2) ===')
  print(t2)
