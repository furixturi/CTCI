# Return Kth to Last: 
# Implement an algorithm to find the kth to last element of a singly
# linked list
from linkedList import LinkedListNode
# Time complexity O(n)
def returnKth(head: LinkedListNode, k) -> int:
  length = 0
  n = head
  while n != None:
    length += 1
    n = n.next
  if length < k:
    return None
  i = length - k
  n = head
  j = 1
  while j < i:
    n = n.next
    j += 1
  return n.data

def printKthRecursive(n: LinkedListNode, k):
  if n == None:
    return -1
  index = printKthRecursive(n.next, k) + 1
  if index == k:
    print(n.data)
  return index

# Time complexity O(n)
# Space complexity O(1)
def returnKthSolution(head: LinkedListNode, k: int) -> int:
  # two pointers
  p1 = head
  p2 = head
  i = 0
  # move p2 k steps away from p1
  while i < k:
    if p2.next == None:
      return None
    p2 = p2.next
    i += 1
  # move p1, p2 together until p2 hits the end
  while p2.next != None:
    p1 = p1.next
    p2 = p2.next
  # p1 is now kth node from the end
  return p1.data

li = LinkedListNode(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
li.append(6)
li.append(7)
li.append(8)
li.append(9)
li.append(10)
print(li)
# print(returnKth(li, 8))
# print(returnKth(li, 2))
# print(returnKth(li, 1))
# print(returnKth(li, 0))
# printKthRecursive(li, 8)
print(returnKthSolution(li, 8))
print(returnKthSolution(li, 0))
print(returnKthSolution(li, 10))