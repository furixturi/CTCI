import random

def quickSort(nums, l=0, r=None):
  if r is None:
    r = len(nums) - 1
  if l < r:
    pIdx = hoare_partition(nums, l, r)
    quickSort(nums, l, pIdx) # use pIdx instead of pIdx-1 to handle duplicate
    quickSort(nums, pIdx+1, r)

def hoare_partition(nums, l, r):
  pivot = nums[l]
  while True:
    while nums[l] < pivot:
      l += 1
    while nums[r] > pivot:
      r -= 1
    if l >= r:
      return r
    nums[l], nums[r] = nums[r], nums[l]
    # to handle duplicate
    l += 1
    r -= 1

nums = [2, 9, 4, 1, 2]
quickSort(nums)
print(nums)
