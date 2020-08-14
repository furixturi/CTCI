class LinkedList:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    res = []
    n = self
    while n != None:
      res.append(n.data)
      n = n.next
    return 'LinkedList: ' + ', '.join([str(d) for d in res])

  def append(self, data):
    n = LinkedList(data)
    c = self
    while c.next != None:
      c = c.next
    c.next = n
  
class HashTable:
  def __init__(self, size=16):
    self.listll = [None]*size
    self.size=size

  def set(self, key, value):
    hashcode = self.hash_func(key)
    index = hashcode % self.size
    if self.listll[index] != None:
      self.listll[index].append(key, value)
    else:
      self.listll[index] = LinkedList((key, value))

  def get(self, key):
    hashcode = self.hash_func(key)
    index = hashcode % self.size
    n = self.listll[index]
    while n != None:
      if n.data[0] == key:
        return n.data[1]
      n = n.next
    return None

  def hash_func(self, key):
    res = 0
    for c in str(key):
      res += ord(c)
    return res