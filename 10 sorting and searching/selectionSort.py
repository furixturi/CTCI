from typing import List
def selectionSort(nums: List[int]):
  n = len(nums)
  for i in range(n-1):
    smallest = nums[i]
    smallestIdx = i
    for j in range(i + 1, n):
      if nums[j] < smallest:
        smallest = nums[j]
        smallestIdx = j
    if smallestIdx != i:
      nums[i], nums[smallestIdx] = nums[smallestIdx], nums[i]

nums = [5, 2, 3, 1, 4]
selectionSort(nums)
print(nums)