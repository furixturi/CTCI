# Search in Rotated Array: Given a sorted array of n integers that has
# been rotated an unknown number of times, write code to find an element
# in the array. You may assume that the array was originally sorted in
# increasing order.
# EXAMPLE
# Input:find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14} 
# Output: 8 (the index of 5 in the array)

def searchRotatedArray(nums, t):
  l = 0
  r = len(nums) - 1
  p = -1
  if nums[l] < nums[r]:
    return bs(nums, t)
  while l < r:
    m = (l + r) // 2
    if nums[m] < nums[r]:
      if nums[m-1] > nums[m]:
        p = m
        break
      r = m-1
    else:
      if nums[m+1] < nums[m]:
        p = m+1
        break
      l = m+1
  rLeft = bs(nums, t, 0, p-1)
  if rLeft != -1:
    return rLeft
  rRight = bs(nums, t, p, r)
  return rRight

def bs(nums, t, l=0, r=None):
  r = len(nums) - 1 if r is None else r
  if l <= r:
    m = (l + r) // 2
    if t == nums[m]:
      return m
    if t < nums[m]:
      return bs(nums, t, l, m-1)
    if t > nums[m]:
      return bs(nums, t, m+1, r)
  return -1

print(searchRotatedArray([3,4,5,1,2],1))
print(searchRotatedArray([3,4,5,1,2],6))

def searchRotatedArrayWithDuplicates(nums, t, l=0, r=None):
  r = len(nums) - 1 if r is None else r
  if l <= r:
    m = (l+r) // 2
    if nums[m] == t: return m
    if nums[l] < nums[m]: # left side sorted
      if nums[m] > t:
        return searchRotatedArrayWithDuplicates(nums, t, l, m-1)
      else:
        return searchRotatedArrayWithDuplicates(nums, t, m+1, r)
    elif nums[l] > nums[m]: # right side sorted
      if nums[m] < t:
        return searchRotatedArrayWithDuplicates(nums, t, m+1, r)
      else:
        return searchRotatedArrayWithDuplicates(nums, t, l, m-1)
    else: # left or right side are all duplicates
      leftResult = searchRotatedArrayWithDuplicates(nums, t, l, m-1)
      if leftResult != -1: return leftResult
      rightResult = searchRotatedArrayWithDuplicates(nums, t, m+1, r)
      return rightResult
  return -1