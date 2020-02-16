# Palindrome: 
# Implement a function to check if a linked list is a palindrome.
from linkedList import LinkedListNode

def is_palindrome(l: LinkedListNode) -> bool:
  if l == None or l.next == None:
    return True
  # a pointer to reference items in LinkedList l
  p = l
  # build a reversed LinkedLinstm adding each item of l to the front
  r = LinkedListNode(l.data)
  while p.next != None:
    p = p.next
    n = LinkedListNode(p.data)
    n.next = r
    r = n
  while l != None and r != None:
    if l.data != r.data:
      return False
    l = l.next
    r = r.next
  return True

def is_palindrome_iterative(l: LinkedListNode) -> bool:
  if l == None or l.next == None:
    return True
  stack = []
  slow = l
  fast = l
  while fast != None and fast.next != None:
    stack.append(slow.data)
    slow = slow.next
    fast = fast.next.next
  # The length is odd number, need to move slow pointer one more step to
  # put it in the middle 
  if fast != None:
    slow = slow.next
  while slow != None:
    data = stack.pop()
    if slow.data != data:
      return False
    slow = slow.next

  return True

def length_of_linkedlist(head: LinkedListNode) -> int:
  length = 0
  while head != None:
    length += 1
    head = head.next
  return length

def is_palindrome_recursive_helper(l: LinkedListNode, length: int) -> (LinkedListNode, bool):
  if length == 1:
    return l.next, True
  if length == 0:
    return l, True
  n, last_result = is_palindrome_recursive_helper(l.next, length-2)
  # return the returned node's next, not the whole list's next
  return n.next, (l.data == n.data and last_result)
  

def is_palindrome_recursive(l: LinkedListNode) -> bool:
  length = length_of_linkedlist(l)
  _, result = is_palindrome_recursive_helper(l, length)
  return result

n = LinkedListNode('a')
n.append('b')
n.append('a')
print(f'{n}: {is_palindrome_recursive(n)}')

n = LinkedListNode('a')
n.append('b')
n.append('c')
print(f'{n}: {is_palindrome_recursive(n)}')

n = LinkedListNode('a')
n.append('b')
n.append('c')
n.append('c')
n.append('b')
n.append('a')
result = is_palindrome_recursive(n)
print(f'{n}: {result}')

n = LinkedListNode('a')
print(f'{n}: {is_palindrome_recursive(n)}')