# Find Duplicates: You have an array with all the numbers from 1 to N,
# where N is at most 32,000. The array may have duplicate entries and
# you do not know what N is. With only 4 kilobytes of memory available,
# how would you print all duplicate elements in the array?

# 4k bytes = 4 * 2^10 * 8 bits = 32768 bits > 32000
def printDuplicate(ints):
  MEMORY_SIZE = 4 * (2 ** 10)
  bv = bytearray(MEMORY_SIZE)
  for int in ints:
    if bv[int//8] & (1<< (int % 8)) == 0:
      bv[int//8] |= 1 << (int % 8)
    else:
      print(int)

printDuplicate([1, 18, 4, 5, 18, 23, 4, 1])