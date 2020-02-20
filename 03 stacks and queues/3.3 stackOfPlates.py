# 3.3 Stack of Plates: 
# Imagine a (literal) stack of plates. If the stack gets too high, 
# it might topple. Therefore, in real life, we would likely start 
# a new stack when the previous stack exceeds some threshold. 
# Implement a data structure SetOfStacks that mimics this. 
# SetOfStacks should be composed of several stacks and should create 
# a new stack once the previous one exceeds capacity. 
# SetOfStacks.push() and SetOfStacks.pop() should behave identically 
# to a single stack (that is, pop() should return the same values as it 
# would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation 
# on a specific sub­ stack.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.height = 0

  def __repr__(self):
    if self.head == None:
      return '[]'
    curr = self.head
    result = []
    while curr != None:
      result.append(repr(curr.data))
      curr = curr.next
    return ' <- '.join(result)

  def push(self, data):
    n = Node(data)
    if self.head == None:
      self.head = n
    else:
      n.next = self.head
      self.head = n
    self.height += 1

  def pop(self):
    if self.head == None:
      raise IndexError('Cannot pop. Stack is empty.')
    n = self.head
    self.head = n.next
    self.height -= 1
    return n.data

  def takeFromBottom(self):
    if self.head == None:
      raise IndexError('Cannot take from bottom. Stack is empty')
    n = self.head
    if n.next == None:
      data = self.head.data
      self.head = None
    else:
      while n.next.next != None:
        n = n.next
      data = n.next.data
      n.next = None
    self.height -= 1
    return data

  def peek(self):
    if self.head == None:
      return None
    else:
      return self.head.data

  def isEmpty(self):
    return self.head == None

class StackOfPlates:
  def __init__(self, threshold = 5):
    self.stacks = [Stack()]
    self.threshold = threshold

  def __str__(self):
    return ' | '.join([ repr(stack) for stack in self.stacks])

  def push(self, data):
    if self.stacks[len(self.stacks) - 1].height == self.threshold:
      self.stacks.append(Stack())
    self.stacks[len(self.stacks) - 1].push(data)

  def pop(self):
    data = self.stacks[len(self.stacks) - 1].pop()
    if self.stacks[len(self.stacks) - 1].height == 0:
      self.stacks.pop()
    return data

  def peek(self):
    return self.stacks[len(self.stacks) - 1].peek()

  def isEmpty(self):
    return len(self.stacks) == 0

  def popAt(self, stackIdx):
    if stackIdx >= len(self.stacks):
      raise IndexError(f'Stack {stackIdx} doesn\'t exist')
    data = self.stacks[stackIdx].pop()
    i = stackIdx + 1
    while i < len(self.stacks):
      self.moveLeft(i)
      i += 1
    return data

  def moveLeft(self, stackIdx):
    fromStack = self.stacks[stackIdx]
    toStack = self.stacks[stackIdx-1]
    data = fromStack.takeFromBottom()
    toStack.push(data)

if __name__ == '__main__':
  plates = StackOfPlates(3)
  plates.push(1)
  plates.push(2)
  plates.push(3)
  plates.push(4)
  plates.push(1)
  plates.push(2)
  plates.push(3)
  plates.push(4)
  print(plates)
  print(plates.popAt(1))
  print(plates)