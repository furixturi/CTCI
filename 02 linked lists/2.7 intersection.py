# Intersection: 
# Given two (singly) linked lists, determine if the two lists intersect. 
# Return the inter­secting node. Note that the intersection is defined 
# based on reference, not value.That is, if the kth node of the first 
# linked list is the exact same node (by reference) as the jth node of 
# the second linked list, then they are intersecting.

from linkedList import LinkedListNode, append_to_last

# time complexity: O(A * B), A is the length of n1, B is the length of n2
# space complexity: O(1)
def intersection_brute_force(n1: LinkedListNode, n2: LinkedListNode) -> LinkedListNode:
  p2 = n2
  while n1 != None:
    p2 = n2
    while p2 != None:
      if n1 == p2:
        return n1
      p2 = p2.next
    n1 = n1.next
  return None

# time complexity: O(A + B)
# space complexity: O(1)
def intersection_solution(n1: LinkedListNode, n2: LinkedListNode) -> LinkedListNode:
  p1 = n1
  p2 = n2
  length1 = 0
  length2 = 0
  # calculate length
  while p1 != None:
    length1 += 1
    p1 = p1.next
  while p2 != None:
    length2 += 1
    p2 = p2.next
  # chop the longer part from the longer list starting from head
  longer_list = n1 if length1 >= length2 else n2
  length_diff = length1 - length2 if length1 >= length2 else length2 - length1
  while length_diff > 0:
    longer_list = longer_list.next
    length_diff -= 1
  if length1 > length2:
    n1 = longer_list
  else:
    n2 = longer_list
  # go through both at the same time
  while n1 != None and n2 != None:
    if n1 == n2:
      return n1
    n1 = n1.next
    n2 = n2.next
  return None



n1 = LinkedListNode(1)
n2 = LinkedListNode(2)
n2.append(4)
n2.append(5)
print(f'n1: {n1}, n2: {n2}')
n3 = LinkedListNode(3)
n3.append(4)
append_to_last(n1, n3)
append_to_last(n2, n3)
print(f'n1: {n1}, n2: {n2}, n3: {n3}')
print(intersection_brute_force(n1, n2))
print(f'{n1}, {n2}, {intersection_solution(n1, n2)}')