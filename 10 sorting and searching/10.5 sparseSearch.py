# Sparse Search: Given a sorted array of strings that is interspersed
# with empty strings, write a method to find the location of a given
# string.
# EXAMPLE
# Input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
# Output: 4

def searchSparce(arr, target):
  searchSparceRec(arr, target, 0, len(arr)-1)

def searchSparceRec(arr, target, start, end):
  if start > end: return -1

  mid = (start + end) // 2
  if arr[mid] == '':
    left = mid-1
    right = mid+1
    while True:
      if left < 0 and right > len(arr) - 1:
        return -1      
      if left >= 0 and arr[left] != '':
        mid = left
        break
      if right <= len(arr)-1 and arr[right] != '':
        mid = right
      left -= 1
      right += 1

  if arr[mid] == target: return mid
  if arr[mid] < target:
    return searchSparceRec(arr, target, mid+1, right)
  return searchSparceRec(arr, target, start, mid-1)