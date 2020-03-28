def heapSort(nums):
  n = len(nums)
  lastLeafNode = n-1
  lastParentNode = (lastLeafNode+1)//2-1

  # convert the nums to a max heap list by calling heapify from the last
  # parent node until to the first item in the nums list
  for i in range(lastParentNode, -1, -1):
    maxHeapify(nums, n, i)

  # sort the list in-place:
  # - swap the first (max) and the last unsorted element, so that the
  #   right end part is sorted
  # - heapify the unsorted part from index 0 to make sure the first is the max of the
  #   unsorted part
  # - keep doing the above until the sorted part covers the whole list
  #   all the way to the first element
  for j in range(n-1, -1, -1):
    nums[0], nums[j] = nums[j], nums[0]
    maxHeapify(nums, j, 0)

# recursively make the i-th to (n-1) part of the nums list a max heap
def maxHeapify(nums, n, i):
  l = 2 * i + 1
  r = 2 * i + 2
  largest = i
  if l < n and nums[l] > nums[largest]:
    largest = l
  if r < n and nums[r] > nums[largest]:
    largest = r
  if largest != i:
    nums[i], nums[largest] = nums[largest], nums[i]
    maxHeapify(nums, n, largest)