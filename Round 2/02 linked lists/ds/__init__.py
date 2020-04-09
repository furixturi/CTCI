class Node:
  def __init__(self, data):
    self.data = data
    self.next =None

  def __repr__(self):
    return str(self.data)

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __repr__(self):
    datas = []
    n = self.head
    while n:
      datas.append(n.data)
      n = n.next
    return ' -> '.join([str(item) for item in datas]) 

  def append(self, data):
    n = Node(data)
    if not self.head:
      self.head = n
      self.tail = n
    else:
      self.tail.next = n
      self.tail = n

  def prepend(self, data):
    n = Node(data)
    if not self.head:
      self.head = n
      self.tail = n
    else:
      n.next = self.head
      self.head = n

  def pop(self):
    if not self.head:
      return None
    t = self.head
    if t == self.tail:
      self.head = None
      self.tail = None
      return t.data
    while t.next != self.tail:
      t = t.next
    data = self.tail.data
    self.tail = t
    t.next = None
    return data

  def popLeft(self):
    if not self.head:
      return None
    h = self.head
    data = h.data
    if h == self.tail:
      self.head = None
      self.tail = None
    else:
      self.head = h.next
    return data

if __name__ == '__main__':
  ll = LinkedList()
  ll.append(1)
  ll.append(2)
  ll.append(3)
  ll.append(4)
  ll.append(5)
  ll.append(6)
  print(ll)
  ll.prepend(0)
  print(ll)
  print(ll.pop())
  print(ll)
  print(ll.popLeft())
  print(ll)