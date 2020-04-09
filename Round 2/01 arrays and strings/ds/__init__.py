class HashTable:
  def __init__(self):
    self.SIZE = 5
    self.list = [None] * self.SIZE

  def set(self, key, value):
    hashCode = self.computeHashCode(key)
    index = hashCode % self.SIZE
    if self.list[index] is None:
      self.list[index] = LinkedList((key, value))
    else:
      self.list[index].append((key, value))

  def get(self, key):
    hashCode = self.computeHashCode(key)
    index = hashCode % self.SIZE
    if self.list[index] is None:
      return None
    ll = self.list[index]
    while True:
      if ll.data[0] == key:
        return ll.data[1]
      ll = ll.next
      if ll is None:
        return None

  def computeHashCode(self, key):
    string = str(key)
    result = 0
    for c in string:
      result += ord(c)
    return result

class LinkedList:
  def __init__(self, data):
    self.data = data
    self.next = None
  
  def append(self, data):
    n = self
    while n.next:
      n = n.next
    n.next = LinkedList(data)
    return self

  def prepend(self, data):
    n = LinkedList(data)
    n.next = self
    return n
    
  def pop(self):
    n = self
    while n.next.next:
      n = n.next
    result = n.next.data
    n.next = None
    return (result, self)

  def popLeft(self):
    n = self
    result = n.data
    newHead = n.next
    n.next = None
    return (result, newHead)

if __name__ == '__main__':
  ht = HashTable()
  ht.set('a', 1)
  ht.set('f', 2)
  print(ht.get('a'))
  print(ht.get('f'))