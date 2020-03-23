from typing import List
# Time: 
#   Best O(n) - already sorted
#   Avg O(n^2)
# Space: O(1)
def insertionSort(nums: List[int]):
  n = len(nums)
  for i in range(1, n):
    curr = nums[i]
    j = i-1
    while j >= 0 and nums[j] > curr:
      nums[j+1] = nums[j]
      j -= 1
    if j != i-1:
      nums[j+1] = curr

nums = [5,4,3,2,1]
insertionSort(nums)
print(nums)