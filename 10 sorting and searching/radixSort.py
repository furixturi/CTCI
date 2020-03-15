# Time: O(kn) k - max number of digits

def calcNumDigits(n):
  if n == 0:
    return 1
  d = 0
  while n >= 1:
    d += 1
    n = n // 10
  return d

def getDigitAt(n, d):
  return n // (10**d) % 10

def sortByDigit(nums, d):
  dMap = [[] for _ in range(10)]
  for n in nums:
    digit = getDigitAt(n, d)
    dMap[digit].append(n)
  i = 0
  for digit in range(10):
    nList = dMap[digit]
    for n in nList:
      nums[i] = n
      i += 1

def radixSort(nums):
  maxNumDigits = 0
  for n in nums:
    nd = calcNumDigits(n)
    if nd > maxNumDigits:
      maxNumDigits = nd
  for d in range(maxNumDigits):
    sortByDigit(nums, d)

nums = [1982, 3, 21354, 5468, 0]
radixSort(nums)
print(nums)