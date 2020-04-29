# LRU Cache: Design and build a "least recently used" cache, which
# evicts the least recently used item. The cache should map from keys to
# values (allowing you to insert and retrieve a value associ­ated with
# a particular key) and be initialized with a max size. When it is full,
# it should evict the least recently used item.
class Node:
  def __init__(self, key):
    self.key = key
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self, key):
    n = Node(key)
    if not self.tail:
      self.head = n
      self.tail = n
    else:
      self.tail.next = n
      n.prev = self.tail
      self.tail = n
    self.size += 1
  
  def appendLeft(self, key):
    n = Node(key)
    if not self.head:
      self.head = n
      self.tail = n
    else:
      self.head.prev = n
      n.next = self.head
      self.head = n
    self.size += 1

  def pop(self):
    if self.size == 0:
      print('List is empty, cannot pop')
      return None
    n = self.tail
    if self.size == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = n.prev
    self.size -= 1
    return n.key

  def popLeft(self):
    if self.size == 0:
      print('List is empty, cannot pop')
      return None
    n = self.head
    if self.size == 1:
      self.head = None
      self.tail = None
    else:
      self.head = n.next
    self.size -= 1
    return n.key

  def moveToHead(self, key):
    curr = self.head
    while True:
      if curr.key == key:
        break
      elif curr.next is None:
        print(f'{key} is not in the list, cannot move')
        return
      else:
        curr = curr.next
    if curr != self.head:
      curr.prev.next = curr.next
      curr.next.prev = curr.prev
      curr.prev = None
      curr.next = self.head
      self.head.prev = curr
      self.head = curr

class LRUCache:
  def __init__(self, maxSize):
    self.maxSize = maxSize
    self.keys = DoublyLinkedList()
    self.map = {}

  def retrieve(self, key):
    if key in self.map:
      self.keys.moveToHead(key)
      return self.map[key]
  
  def insert(self, key, value):
    if key not in self.map:
      if self.keys.size == self.maxSize:
        LRUKey = self.keys.pop()
        del self.map[LRUKey]
      self.keys.appendLeft(key)
    else:
      self.keys.moveToHead(key)
    self.map[key] = value
