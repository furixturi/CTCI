def mergeSort(nums):
  if len(nums) == 1:
    return nums
  mid = len(nums) // 2
  return merge(mergeSort(nums[0:mid]), mergeSort(nums[mid:]))

def merge(left, right):
  l = 0
  r = 0
  result = []
  while l < len(left) and r < len(right):
    if left[l] <= right[r]:
      result.append(left[l])
      l += 1
    else:
      result.append(right[r])
      r += 1
  if l < len(left):
    result += left[l:]
  if r < len(right):
    result += right[r:]
  return result

l = [3, 5, 2, 4, 1, 3]
print(mergeSort(l))