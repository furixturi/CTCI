# time: average and worst O(n^2)
# space: O(1)
from typing import List
def bubbleSort(nums: List[int]):
  n = len(nums)
  for i in range(n-1):
    for j in range(n-i-1):
      if nums[j] > nums[j+1]:
        nums[j], nums[j+1] = nums[j+1], nums[j]

nums = [5, 4, 3, 2, 1]
bubbleSort(nums)
print(nums)