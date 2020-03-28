# PeaksandValleys:In an array of integers,a "peak" is an element which is
# greater than or equal to the adjacent integers and a "valley" is an element 
# which is less than or equal to the adjacent inte­gers. 
# For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and 
# {5, 2} are valleys. Given an array of integers, sort the array into an 
# alternating sequence of peaks and valleys.
# EXAMPLE
# Input: {5, 3, 1, 2, 3}
# Output: {5, 1, 3, 2, 3}

def peaksAndValleys(nums):
  numsSorted = sorted(nums)
  n = len(nums)
  choosePeak = True
  for i in range(n):
    if choosePeak:
      nums[i] = numsSorted[(n-1-i//2)]
    else:
      nums[i] = numsSorted[i//2]
    choosePeak = not choosePeak

def solutionSuboptimal(nums):
  nums.sort()
  for i in range(1, len(nums), 2):
    nums[i], nums[i-1] = nums[i-1], nums[i]

def solutionOptimal(nums):
  for i in range(1, len(nums), 2):
    maxIdx = getNeighborMaxIdx(nums, i)
    if maxIdx != i:
      nums[maxIdx], nums[i] = nums[i], nums[maxIdx]

def getNeighborMaxIdx(nums, i):
  maxIdx = i
  if i-1 >= 0 and nums[i-1] > nums[maxIdx]:
    maxIdx = i-1
  if i+1 < len(nums) and nums[i+1] > nums[maxIdx]:
    maxIdx = i+1
  return maxIdx

if __name__ == '__main__':
  nums = [5,3,1,2,3]
  peaksAndValleys(nums)
  print(nums)
  nums2 = [5,3,1,2,3]
  solutionSuboptimal(nums2)
  print(nums2)
  nums3 = [5,3,1,2,3]
  solutionOptimal(nums3)
  print(nums3)