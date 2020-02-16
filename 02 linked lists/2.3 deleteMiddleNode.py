# Delete Middle Node: 
# Implement an algorithm to delete a node in the middle (i.e., any node 
# but the first and last node, not necessarily the exact middle) of a 
# singly linked list, given only access to that node.
# EXAMPLE
# lnput:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like
# a->b->d->e->f
from linkedList import LinkedListNode
def deleteMiddle(middleNode: LinkedListNode) -> bool:
  if middleNode.next == None:
    return False
  middleNode.data = middleNode.next.data
  middleNode.next = middleNode.next.next
  return True

li = LinkedListNode('a')
li.append('b')
li.append('c')
li.append('d')
li.append('e')
li.append('f')
print(li)
deleteMiddle(li.getNode('c'))
print(li)