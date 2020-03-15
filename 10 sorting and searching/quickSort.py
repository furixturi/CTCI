from typing import List

def quickSort(nums, l = 0, r = None):
  if r is None:
    r = len(nums) - 1
  if l < r:
    pIdx = partition(nums, l, r)
    quickSort(nums, l, pIdx-1)
    quickSort(nums, pIdx + 1, r)

def partition(nums, l, r):
  pivot = nums[(l + r) // 2]
  while l < r:
    while nums[l] < pivot:
      l += 1
    while nums[r] > pivot:
      r -= 1
    if l == r:
      return l
    nums[l], nums[r] = nums[r], nums[l]

nums = [5, 4, 1, 3, 2]
quickSort(nums)
print(nums)