# A queue implements FIFO (first-in first-out) ordering. 
# As in a line or queue at a ticket stand, items are removed from 
# the data structure in the same order that they are added.
# It uses the operations:
# add(itern): Add an item to the end of the list. 
# remove(): Remove the first item in the list.
# peek() : Return the top of the queue.
# is_empty(): Return true if and only if the queue is empty.

from typing import TypeVar, List
T = TypeVar('T')

class QueueNode:
  def __init__(self, data: T):
    self.data = data
    self.next = None
    self.prev = None

class Queue:
  def __init__(self, items: List[T] = []):
    self.head = None
    self.tail = None
    self.length = len(items)
    last = None
    for (i, data) in enumerate(items):
      curr = QueueNode(data)
      if i == 0:
        self.head = curr
      if i == len(items) - 1:
        self.tail = curr
      if last != None:
        curr.prev = last
        last.next = curr
      last = curr
  
  def __repr__(self) -> str:
    if self.length == 0:
      return 'Queue: empty'
    items = []
    n = self.head
    while n != None:
      items.append(str(n.data))
      n = n.next
    items_str = ' -> '.join(items)
    return f'Queue: {items_str}'

  def enqueue(self, item: T):
    n = QueueNode(item)
    if self.length == 0:
      self.head = n
      self.tail = n
    else:
      self.tail.next = n
      n.prev = self.tail
      self.tail = n
    self.length += 1

  def dequeue(self) -> T:
    if self.length == 0:
      raise IndexError('Queue is empty, nothing to remove.')
    data = self.head.data
    self.head = self.head.next
    self.head.prev = None
    self.length -= 1
    if self.length == 1:
      self.tail.prev = None
    if self.length == 0:
      self.tail = None
    return data

  def peek(self) -> T:
    if self.length == 0:
      return None
    return self.head.data

  def is_empty(self) -> bool:
    return self.length == 0

if __name__ == '__main__':
  q = Queue([1,9,8,3,0,4,2,1])
  print(q.is_empty())
  print(q)
  q.enqueue('wow')
  print(q)
  print(q.dequeue())
  print(q)
  print(q.peek())
  