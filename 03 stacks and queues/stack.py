# A stack 
# uses LIFO (last-in first-out) ordering. 
# It uses the following operations:
# - pop(): Remove the top item from the stack. 
# - push(item): Add an item to the top of the stack. 
# - peek(): Return the top of the stack.
# - is_empty (): Return true if and only if the stack is empty.

from typing import List, TypeVar
T = TypeVar('T')
class StackWithList:
  def __init__(self, items: List[T] = []):
    self.items = items
    self.length = len(items)
  
  def __repr__(self) -> str:
    return f'Stack {self.items}'

  def pop(self) -> T:
    item = self.items.pop()
    self.length -= 1
    return item
  
  def push(self, item) -> None:
    self.items.append(item)
    self.length += 1

  def peek(self) -> T:
    return self.items[self.length-1]

  def is_empty(self) -> bool:
    return self.length == 0

from LinkedListNode import LinkedListNode, from_list
class Stack:
  def __init__(self, items: List = []):
    if len(items) != 0:
      self.items = from_list(items)
    else:
      self.items = None
  
  def __repr__(self) -> str:
    if self.items == None:
      return 'Stack empty'
    return f'Stack {self.items}'
  
  def push(self, data: T) -> None:
    if self.items == None:
      self.items = LinkedListNode(data)
    else:
      self.items = self.items.insert_head(data)

  def pop(self) -> T:
    if self.items == None:
      return None
    data, self.items = self.items.get_head()
    return data

  def peek(self) -> T:
    if self.items == None:
      return None
    return self.items.data

  def is_empty(self) -> bool:
    return self.items == None


if __name__ == '__main__':
  s = Stack()
  print(f'initialize an empty Stack: {s}')
  print(f's.is_empty(): {s.is_empty()}')
  s = Stack([1,2,3])
  print(f'initialize a Stack from List [1,2,3]: {s}')
  print(f's.peek(): {s.peek()}')
  print(f's.pop(): {s.pop()}')
  print(f'after pop: {s}')
  s.push(4)
  print(f'after f.push(4): {s}')
  print(f's.is_empty(): {s.is_empty()}')
