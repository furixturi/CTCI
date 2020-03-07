# Magic Index: A magic index in an array A[0••• n - 1] is defined to be 
# an index such that A[i] = i. Given a sorted array of distinct integers, 
# write a method to find a magic index, if one exists, in array A.
# FOLLOW UP
# What if the values are not distinct?
import math
def findMagicIndex(list, start = None, end = None):
  if not list:
    return None

  start = 0 if start is None else start
  end = len(list) - 1 if end is None else end

  if end < start:
    return -1

  middle = (start + end) // 2
  if list[middle] == middle:
    return middle
  elif list[middle] > middle:
    return findMagicIndex(list, start, middle-1)
  else:
    return findMagicIndex(list, middle + 1, end)

def magicIndexWithDuplicate(list, start= None , end = None):
  if not list:
    return -1
  start = 0 if start is None else start
  end = len(list) - 1 if end is None else end

  if start > end:
    return -1

  middle = (start + end) // 2
  if list[middle] == middle:
    return middle

  # elif list[middle] < middle:
  #   if list[middle] >= start:
  #     left = magicIndexWithDuplicate(list, start, list[middle])
  #     if left > -1:
  #       return left
  #   return magicIndexWithDuplicate(list, middle + 1, end)
  # else:
  #   if list[middle] <= end:
  #     right = magicIndexWithDuplicate(list, list[middle], end)
  #     if right > -1:
  #       return right
  #   return magicIndexWithDuplicate(list, start, middle - 1)
  left = magicIndexWithDuplicate(list, start, min(middle-1, list[middle]))
  if left > -1:
    return left
  right = magicIndexWithDuplicate(list, max(middle+1, list[middle]), end)
  return right


list = [-9, 1, 5, 6, 9, 12]
print(findMagicIndex(list))
list = [-9, 0, 5, 6, 9, 12]
print(findMagicIndex(list))


list = [-9, 1, 1, 6, 9, 12]
print(findMagicIndex(list))
print(magicIndexWithDuplicate(list))
list = [-9, 0, 5, 6, 6, 12]
print(magicIndexWithDuplicate(list))