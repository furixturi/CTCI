# Loop Detection: 
# Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's 
# next pointer points to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C[thesameCasearlier]
# Output: C
from typing import Optional
from linkedList import LinkedListNode, append_to_last

# time complexity: O(N)
# space complexity: O(N)
def loop_detection(l: LinkedListNode) -> Optional[LinkedListNode]:
  mem = set()
  while l != None:
    if l in mem:
      return l
    mem.add(l)
    l = l.next
  return None

def loop_detection_solution(l: LinkedListNode) -> Optional[LinkedListNode]:
  if l == None or l.next == None or l.next.next == None:
    return None
  s = l
  f = l
  while f != None and f.next != None:
    s = s.next
    f = f.next.next
    if s == f:
      break
  # f reached the end without colliding with s, no loop
  if f == None or f.next == None:
    return None
  # f and s collided
  # move f to the head, move both s and f one step ahead each time until
  # they collide again
  f = l
  while s != f:
    s = s.next
    f = f.next
  # now both end up at the start of the loop
  return s


n = LinkedListNode(1)
n.append(2)
n.append(3)
n.append(4)
n.append(5)
n.append(6)
p = n
i = 0
while i < 3:
  p = p.next
  i += 1
append_to_last(n, p)

print(loop_detection(n))