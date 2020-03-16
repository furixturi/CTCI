# Sorted Search, No Size: You are given an array-like data structure
# Listy which lacks a size method. It does, however, have an
# elementAt(i) method that returns the element at index i in 0( 1) time.
# If i is beyond the bounds of the data structure, it returns -1. (For
# this reason, the data structure only supports positive integers.)
# Given a Listy which contains sorted, positive integers, find the index
# at which an element x occurs. If x occurs multiple times, you may
# return any index.
def searchListy(nums, t, l = 0, r = None):
  # if nums[l] == -1:
  if l >= len(nums):
    return -1
  if nums[l] == t: return l
  r = t - nums[l] + l if r is None else r
  if l <= r:
    if r < len(nums) and nums[r] == t: return r
    # if nums[r] == -1: 
    if r >= len(nums): 
      r = r // 2
    elif nums[r] < t:
      l = r + 1
      r = r * 2
    else: # nums[r] > t
      m = (l + r) // 2
      if nums[m] == t: return t
      if nums[m] < t:
        l = m+1
      else:
        r = m-1
    return searchListy(nums, t, l, r)
  return -1

print(searchListy([1,3,5], 0))
print(searchListy([1,3,5], 1))
print(searchListy([1,3,5], 2))
print(searchListy([1,3,5], 5))
print(searchListy([1,3,5], 6))