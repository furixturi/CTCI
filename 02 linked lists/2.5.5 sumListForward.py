# FOLLOW UP
# Suppose the digits are stored in forward order. 
# Repeat the above problem. EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. 
# Output:9 -> 1 -> 2.That is, 912.

from linkedList import LinkedListNode

def length(n: LinkedListNode) -> int:
  i = 0
  while n != None:
    i += 1
    n = n.next
  return i

def test_length():
  print('== test length(n: LinkedListNode) >>')
  n = LinkedListNode(1)
  print(f'Expected : 1; Actual: {str(length(n))}')
  n.append(2)
  print(f'Expected : 2; Actual: {str(length(n))}')
  n.append(3)
  print(f'Expected : 3; Actual: {str(length(n))}')

# test_length()

def pad_left(n: LinkedListNode, num: int) -> LinkedListNode:
  if num <= 0:
    return n
  head = LinkedListNode(0)
  i = 1
  while i < num:
    head.append(LinkedListNode(0))
  head.append(n)
  return head

def test_pad_left():
  n = LinkedListNode(1)
  n.append(2)
  padded = pad_left(n, 1)
  print(f'Expected: 0 -> 1 -> 2; Actual: {padded}')

# test_pad_left()

def insert_before(n: LinkedListNode, data: int) -> LinkedListNode:
  new_node = LinkedListNode(data)
  new_node.next = n
  return new_node

def addListNodeHelper(n1: LinkedListNode, n2: LinkedListNode) -> (LinkedListNode, int):
  if n1 == None and n2 == None:
    return None, 0
  result, carry = addListNodeHelper(n1.next, n2.next)
  sum = carry
  if n1 != None:
    sum += n1.data
  if n2 != None:
    sum += n2.data
  data = sum % 10
  carry = sum // 10
  result = insert_before(result, data)
  return result, carry

def addListForward(n1: LinkedListNode, n2: LinkedListNode) -> LinkedListNode:
  l1 = length(n1)
  l2 = length(n2)
  if l1 >= l2:
    n2 = pad_left(n2, length(n1) - length(n2))
  else:
    n1 = pad_left(n1, length(n2) - length(n1))
  result, carry = addListNodeHelper(n1, n2)
  # If there is a carry left over, 
  # insert it at the front of the result list
  if carry != 0:
    result = insert_before(result, carry)
  return result

# test
n1 = LinkedListNode(9)
n1.append(8)
n1.append(9)
n2 = LinkedListNode(5)
n2.append(7)
n2.append(8)
n3 = addListForward(n1, n2)
print(n3)
