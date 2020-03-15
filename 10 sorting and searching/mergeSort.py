from typing import List

def mergeSort(nums: List[int]):
  mergeSortRecursive(nums, 0, len(nums)-1)

def mergeSortRecursive(nums, start, end):
  if start < end:
    middle = (start + end) // 2
    mergeSortRecursive(nums, start, middle)
    mergeSortRecursive(nums, middle+1, end)
    merge(nums, start, middle, end)

def merge(nums, start, middle, end):
  left = nums[start:middle+1]
  right = nums[middle+1:end+1]
  leftIdx = 0
  rightIdx = 0
  currIdx = start

  while leftIdx < len(left) and rightIdx < len(right):
    if left[leftIdx] <= right[rightIdx]:
      nums[currIdx] = left[leftIdx]
      leftIdx += 1
    else:
      nums[currIdx] = right[rightIdx]
      rightIdx += 1
    currIdx += 1

  while leftIdx < len(left):
    nums[currIdx] = left[leftIdx]
    leftIdx += 1
    currIdx += 1

nums = [5, 2, 4, 1, 3]
mergeSort(nums)
print(nums)