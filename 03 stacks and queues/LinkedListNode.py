# to reference LinkedListNode type inside its own class
from __future__ import annotations
from typing import TypeVar, List
T = TypeVar('T')

class LinkedListNode:
  def __init__(self, data: T):
    self.data = data
    self.next = None
  
  def __repr__(self) -> str:
    items = []
    p = self
    while p != None:
      items.append(str(p.data))
      p = p.next
    list_str = ' -> '.join(items)
    return f'LinkedList {list_str}'

  def append_tail(self, data: T):
    t = LinkedListNode(data)
    n = self
    while n.next != None:
      n = n.next
    n.next = t
  
  def remove_tail(self) -> (T, LinkedListNode):
    if self == None:
      return None, None
    if self.next == None:
      data = self.data
      self = None
      return data, None
    l = self
    n = self.next
    while n.next != None:
      l = l.next
      n = n.next
    data = n.data
    l.next = None
    return data, self

  def insert_head(self, data: T):
    h = LinkedListNode(data)
    h.next = self
    return h
  
  def get_head(self) -> (T, LinkedListNode):
    data = self.data
    self = self.next
    return data, self

def from_list(items: List[T]) -> LinkedListNode:
  n = LinkedListNode(items[0])
  for i in range(1, len(items)):
    data = items[i]
    n.append_tail(data)
  return n 

if __name__ == '__main__':
  l = from_list([1,2])
  print(l)
