# Partition: 
# Write code to partition a linked list around a value x, such that all 
# nodes less than x come before all nodes greater than or equal to x. 
# If x is contained within the list, the values of x only need to be after 
# the elements less than x (see below). The partition element x can appear 
# anywhere in the "right partition"; it does not need to appear between 
# the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] 
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# Can't do it in place with the original LinkedList
# Need to set n.next = None
from linkedList import LinkedListNode
def partition(n: LinkedListNode, partition) -> LinkedListNode:
  s_start = None
  s_end = None
  l_start = None
  l_end = None

  while n != None:
    next = n.next
    n.next = None # THIS IS IMPORTANT! Otherwise you leak memory
    if n.data < partition:
      if s_start == None:
        s_start = n
        s_end = s_start
      else:
        s_end.next = n
        s_end = n
    else:
      if l_start == None:
        l_start = n
        l_end = l_start
      else:
        l_end.next = n
        l_end = n
    n = next
  if s_start == None:
    return l_start
  s_end.next = l_start
  return s_start

li = LinkedListNode(5)
li.append(8)
li.append(3)
li.append(5)
li.append(10)
li.append(2)
li.append(1)
print(li)
print(partition(li, 5))