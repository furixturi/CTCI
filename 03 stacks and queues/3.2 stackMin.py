# 3.2 Stack Min: 
# How would you design a stack which, in addition to push and pop, 
# has a function min which returns the minimum element? 
# Push, pop and min should all operate in 0(1) time.

class StackNode:
  def __init__(self, data):
    self.data = data
    self.next = None
  
  def __repr__(self):
    return f'{repr(self.data)}'

class Stack:
  def __init__(self, data = None):
    if data != None:
      self.head = StackNode(data)
    else:
      self.head = None

  def __repr__(self):
    result = []
    curr = self.head
    while curr != None:
      result.append(repr(curr))
      curr = curr.next
    return ' <- '.join(result)

  def push(self, data):
    n = StackNode(data)
    old_head = None if self.head == None else self.head
    n.next = old_head
    self.head = n

  def pop(self):
    n = self.head
    if n == None:
      raise IndexError(f'Stack is empty, cannot pop.')
    self.head = n.next
    n.next = None
    return n.data

  def peek(self):
    if self.head != None:
      return self.head.data
    else:
      return None

  def is_empty(self):
    return self.head == None

class StackWithMin(Stack):
  def __init__(self, data = None):
    Stack.__init__(self, data)
    self.minStack = Stack()
    if data != None:
      self.minStack.push(data)
  
  def push(self, data):
    currMin = self.minStack.peek()
    Stack.push(self, data)
    if currMin == None or currMin >= data:
      self.minStack.push(data)
    
  def pop(self):
    n = Stack.pop(self)
    if n != None and n == self.minStack.peek():
      self.minStack.pop()
    return n

  def get_min(self):
    return self.minStack.peek()

if __name__ == '__main__':
  s = StackWithMin()
  # print(s)
  s.push(5)
  s.push(2)
  s.push(8)
  s.push(2)
  s.pop()
  s.pop()
  s.pop()
  print('END')
