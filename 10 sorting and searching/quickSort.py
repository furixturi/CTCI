from typing import List

def quickSort(nums, l = 0, r = None):
  if r is None:
    r = len(nums) - 1
  if l < r:
    pIdx = partition(nums, l, r)
    quickSort(nums, l, pIdx-1)
    quickSort(nums, pIdx + 1, r)

def partition(nums, l, r):
  end = r
  pivot = nums[(l + r) // 2]
  while l < r:
    while nums[l] < pivot and l < r:
      l += 1
    while nums[r] >= pivot and l < r:
      r -= 1
    nums[l], nums[r] = nums[r], nums[l]
  if nums[l] >= nums[end]:
    nums[l], nums[end] = nums[end], nums[l]
  else:
    l += 1
  return l
    

nums = [5, 2, 9, 1, 4]
nums2 = [5, 3, 2, 1, 9, 2]
# quickSort(nums)
quickSort(nums2)
# print(nums)
print(nums2)