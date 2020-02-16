# Sum Lists: 
# You have two numbers represented by a linked list, where each node 
# contains a single digit.The digits are stored in reverse order, such 
# that the 1's digit is at the head of the list. Write a function that 
# adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. 
# Output:2 -> 1 -> 9.That is,912.
# FOLLOW UP
# Suppose the digits are stored in forward order. 
# Repeat the above problem. EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. 
# Output:9 -> 1 -> 2.That is, 912.
from linkedList import LinkedListNode
def numFromList(n: LinkedListNode) -> int:
  d = 0
  num = 0
  while n != None:
    num += n.data * 10**d
    d += 1
    n = n.next
  return num

def listFromNum(num: int) -> LinkedListNode:
  num_str = str(num)
  li: LinkedListNode = None
  for i in range(len(num_str)-1, -1, -1):
    if li == None:
      li = LinkedListNode(int(num_str[i]))
    else:
      li.append(int(num_str[i]))
  return li

def sumLists(n1: LinkedListNode, n2: LinkedListNode) -> LinkedListNode:
  num1 = numFromList(n1)
  num2 = numFromList(n2)
  sum = num1 + num2
  return listFromNum(sum)

def sumListsSolution(n1: LinkedListNode, n2: LinkedListNode, carry: int = 0) -> LinkedListNode:
  if n1 == None and n2 == None and carry == 0:
    return None
  value = carry
  if n1 != None:
    value += n1.data
  if n2 != None:
    value += n2.data
  carry = value // 10
  n = LinkedListNode(value % 10)

  if n1.next != None or n2.next != None or carry != 0:
    n1_next = n1.next if n1 != None else None
    n2_next = n2.next if n2 != None else None
    next = sumListsSolution(n1_next, n2_next, carry)
    n.next = next
  
  return n



n1 = LinkedListNode(7)
n1.append(1)
n1.append(6)
n2 = LinkedListNode(5)
n2.append(9)
n2.append(2)
print(f'n1: {n1}')
print(f'n2: {n2}')
print(f'sum: {sumLists(n1, n2)}')
print(f'sum: {sumListsSolution(n1, n2)}')

