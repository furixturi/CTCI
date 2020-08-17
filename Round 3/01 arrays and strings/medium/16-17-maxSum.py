# Contiguous Sequence: You are given an array of integers (both positive
# and negative). Find the contiguous sequence with the largest sum.
# Return the sum.
# EXAMPLE
# lnput: 2, -8, 3, -2, 4, -10 Output:5 (i.e•, {3, -2, 4})

def maxSum(l):
  currSum = 0
  currSumStart = 0
  currSumEnd = 0
  maxSum = 0
  maxSumStart = 0
  maxSumEnd = 0
  for i in range(len(l)):
    n = l[i]
    currSum += n
    currSumEnd = i
    if currSum > maxSum:
      maxSum = currSum
      maxSumStart = currSumStart
      maxSumEnd = currSumEnd
    elif currSum < 0:
      currSum = 0
      currSumStart = i+1
      currSumEnd = i+1
  return maxSum, (maxSumStart, maxSumEnd)

if __name__ == '__main__':
  print(maxSum([2,-8,3,-2,4,-10]))
  print(maxSum([2, 3, -8, -1, 2, 4, -2, 3]))
