# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
from ds import LinkedList

# O(N) time, O(N) space
def removeDups(ll: LinkedList):
  last = None
  current = ll.head
  tab = set()
  while current:
    if current.data in tab:
      last.next = current.next
    else:
      tab.add(current.data)
      last = current
    current = current.next

# Follow up: O(N^2) time, O(1) space
def removeDupsNoBuffer(ll: LinkedList):
  current = ll.head
  while current:
    runner = current
    while runner.next:
      if runner.next.data == current.data:
        runner.next = runner.next.next
      else:
        runner = runner.next
    current = current.next      


ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(4)
ll.append(6)
ll.append(1)

print(ll)
# removeDups(ll)
removeDupsNoBuffer(ll)
print(ll)