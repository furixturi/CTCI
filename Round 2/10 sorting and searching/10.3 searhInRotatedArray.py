def searchRotatedList(li, target):
  oriStart = findSmallest(li)
  result = binarySearch(li, target, oriStart, len(li)-1)
  if result == -1:
    result = binarySearch(li, target, 0, oriStart-1)
  return result

def findSmallest(li, start=0, end=None):
  if end is None: end = len(li) - 1
  if li[start] == li[end]:
    while li[end] == li[start]:
      end -= 1
    if end < start:
      return start
  mid = (start + end) // 2
  if li[start] <= li[mid]:
    if li[mid] <= li[end]: return start
    return findSmallest(li, mid+1, end)
  return findSmallest(li, start, mid)

def binarySearch(li, target, start=0, end=None):
  if end is None: end = len(li) - 1
  if start <= end:
    mid = (start + end) // 2
    if li[mid] == target:
      while mid > start and li[mid-1] == target:
        mid -= 1
      return mid
    if li[mid] < target:
      return binarySearch(li, target, mid+1, end)
    return binarySearch(li, target, start, mid-1)
  return -1


# print(findSmallest([0,1,2,3,4]))
# print(findSmallest([3,4,0,1,2]))
# print(findSmallest([3,0,1,2,3]))
# print(findSmallest([1,2,3,4,0]))
# print(findSmallest([1,2,2,3,4,0]))
# print(findSmallest([0,1,2,3,4,0]))
# print(findSmallest([2,3,4,0,0,1,2]))
# print(findSmallest([1,1,2,2,3,4,0,0]))
# print(findSmallest([0,1,1,2,2,3,4,0,0]))

# print(binarySearch([0, 0, 1, 2, 2, 3, 5], 4))
# print(binarySearch([0, 0, 1, 2, 2, 3, 5], 3))
# print(binarySearch([0, 0, 1, 2, 2, 3, 5], 2))
# print(binarySearch([0, 0, 1, 2, 2, 3, 5], 1))
# print(binarySearch([0, 0, 1, 2, 2, 3, 5], 5))
# print(binarySearch([0, 0, 1, 2, 2, 3, 5], 0))

print(searchRotatedList([0,1,2,3,4,0], 0))
print(searchRotatedList([0,1,2,3,3,4,0], 3))
print(searchRotatedList([0,1,2,3,3,4,0], 5))