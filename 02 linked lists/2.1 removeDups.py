# Remove Dups: 
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from linkedList import LinkedListNode, printLinkedList

def removeDups(head: LinkedListNode):
  mem = {
    str(head.data): True
  }
  n = head
  while n.next != None:
    while n.next != None and str(n.next.data) in mem:
      n.next = n.next.next
    if n.next != None:
      mem[str(n.next.data)] = True
      n = n.next
  # print(mem)
  # return head

# Time complexity O(n)
# Space complexity O(n)
def removeDupsSolution(head: LinkedListNode):
  mem = set()
  n = head
  previous = None
  while n != None:
    if n.data in mem:
      previous.next = n.next
    else:
      mem.add(n.data)
      previous = n
    n = n.next

# Time complexity O(n^2)
# Space complexity O(1)
def removeDupsNoBuffer(head: LinkedListNode):
  if head.next == None:
    return
  n1 = head
  prev = head
  while n1 != None:
    prev = n1
    n2 = n1.next
    while n2 != None:
      if n1.data == n2.data:
        prev.next = n2.next
      else:
        prev = n2
      n2 = n2.next
    n1 = n1.next
    


head: LinkedListNode = LinkedListNode(2)
head.append(2)
head.append(3)
head.append(3)
head.append(2)
head.append(5)
head.append(1)
head.append(1)
head.append(1)
head.append(4)
print(head)
# removeDupSolution(head)
# removeDupSolution(head)
removeDupsNoBuffer(head)
print(head)