def binarySearch(nums, t):
  left = 0
  right = len(nums) - 1
  while left <= right:
    middle = (left + right) // 2
    if t == nums[middle]:
      return middle
    if t < nums[middle]:
      right = middle - 1
    else:
      left = middle + 1
  return -1

def bsr(nums, t, l = 0, r = None):
  r = len(nums) - 1 if r is None else r
  if l <= r:
    m = (l + r) // 2
    if t == nums[m]:
      return m
    if t < nums[m]:
      return bsr(nums, t, l, m-1)
    if t > nums[m]:
      return bsr(nums, t, m+1, r)
  return -1
  