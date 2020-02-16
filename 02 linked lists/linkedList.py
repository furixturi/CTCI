def printLinkedList(head):
  mem = set()
  data_list = []
  n = head
  while n != None and n not in mem:
    data_list.append(str(n.data))
    mem.add(n)
    n = n.next
  return ' -> '.join(data_list)

class LinkedListNode:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    return printLinkedList(self)
  
  def append(self, data):
    newTail: LinkedListNode = LinkedListNode(data)
    n = self
    while n.next != None:
      n = n.next
    n.next = newTail

  def getNode(self, data):
    n = self
    while n != None:
      if n.data == data:
        return n
      n = n.next
    return None

def deleteNode(head: LinkedListNode, data) -> LinkedListNode:
  n = head
  # if it is head
  if n.data == data:
    # move head
    return n.next
  # otherwise, go through each n until the end
  while n.next != None:
    if n.next.data == data:
      n.next = n.next.next
      return head
    n = n.next
  return head

def append_to_last(l: LinkedListNode, n: LinkedListNode):
  p = l
  while p != None and p.next != None:
    p = p.next
  p.next = n

if __name__ == '__main__':
  node = LinkedListNode(3)
  node.append(4)
  node.x = 'whatevs'
  print(node.data)
  print(node.next.data)
  print(node.x)
  printLinkedList(node)