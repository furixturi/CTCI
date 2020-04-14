# Stack Min: How would you design a stack which, in addition to push and
# pop, has a function min which returns the minimum element? Push, pop
# and min should all operate in 0(1) time.
import math
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None

  def __repr__(self):
    n = self.head
    datas = []
    while n:
      datas.append(n.data)
      n = n.next
    return ' -> '.join([str(data) for data in datas])

  def push(self, data):
    n = Node(data)
    n.next = self.head
    self.head = n

  def pop(self):
    h = self.head
    if h is None:
      return None
    newHead = h.next
    h.next = None
    self.head = newHead
    return h.data

  def peek(self):
    if self.head:
      return self.head.data
    return None
class StackMin(Stack):
  def __init__(self):
    super().__init__()
    self.minStack = Stack()

  def push(self, data):
    super().push(data)
    if self.minStack.peek() is None or data <= self.minStack.peek():
      self.minStack.push(data)

  def pop(self):
    result = super().pop()
    if self.minStack.peek() == result:
      self.minStack.pop()
    return result

  def getMin(self):
    return self.minStack.peek()

if __name__ == '__main__':
  ms = StackMin()
  ms.push(256)
  print(ms)
  print(ms.getMin()) # 256
  ms.push(1)
  ms.push(46)
  print(ms)
  print(ms.getMin()) # 1
  ms.push(1)
  ms.push(-1)
  print(ms)
  print(ms.getMin()) # -1
  ms.pop()
  print(ms)
  print(ms.getMin()) # 1
  ms.pop()
  print(ms)
  print(ms.getMin()) # 1
  