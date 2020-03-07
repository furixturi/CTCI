# Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have
#  3 towers and N disks of different sizes which can slide onto any tower. 
#  The puzzle starts with disks sorted in ascending order of size from top 
#  to bottom (i.e., each disk sits on top of an even larger one).You have 
#  the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
#  Write a program to move the disks from the first tower to the last
#  using stacks.

def hanoi(n, s1, s2, s3):
  if n <= 0: # base case, no disks to move
    return
  hanoi(n-1, s1, s3, s2) # move the top n-1 disks from source tower to buffer tower
  s3.append(s1.pop()) # move the biggest disk from source to destination tower
  hanoi(n-1, s2, s1, s3) # move the top n-1 disks from buffer tower to destination tower
  return

stack1 = [5,4,3,2,1]
stack2 = []
stack3 = []
hanoi(5, stack1, stack2, stack3)
print(stack1, stack2, stack3)