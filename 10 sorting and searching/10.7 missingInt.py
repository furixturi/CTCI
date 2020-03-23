# Missing Int: Given an input file with four billion non-negative
# integers, provide an algorithm to generate an integer that is not
# contained in the file. Assume you have 1 GB of memory available for
# this task.

# Solution Note:
# 1 GB RAM = 1 billion bytes = 8 billion bits
# Java integer is 32 bit, between -2,147,483,648 ~ 2,147,483,647 (-2^31 ~ 2^31-1)
# aka. there are 2^32 = 4 billion = 4GB total possible value including 
# negative int, 0, and positive, so if negative integer is also included, 
# we need 4GB/8 = 512 MB memory to save this many possibilities) 

# However, since Java doesn't provide unsigned integer type and we know the four
# billion integers are "non-negative", we know that these integers are between
# 0 ~ 2^31-1


# A bit vector to store a true/false flag for all of them would take
# 2^31 bits = 2^28 bytes = 2^18 Kilobytes = 2^8 MB = 256 MB
# This can be implemented using a byte array, with each item
# representing 8 integer's found/not found status with 1/0

def missingIntWith1G(ints):
  INT_MAX = 2 ** 31
  bvs = bytearray(INT_MAX)
  for integer in ints:
    # 1 left shift (<<) integer % 8 gives us a byte with only the
    # (integer % 8) position set to 1
    # Then use bitwise OR to set the bit vector's last result's integer
    # % 8 position to 1 (if it is not already 1)
    bvs[integer // 8] |= 1 << integer % 8 
  # need the index to calculate the original integer's bigger part
  # except the last part (% 8)
  for i in range(len(bvs)):
    b = bvs[i]
    # find if a bit position in that byte is 0 by using a bitwise AND
    # with a 1 bitwise left shifted each bit position (e.g., to check
    # the 3rd position, use 1 << 3 = '00001000')
    # If the original number's that binary position is 1, this operation
    # will return the 1 << x itself's value. Otherwise, it returns 0,
    # e.g, to find which binary position of 239 is zero:
    # 239 (11101111) & (1 << 0) (= 00000001, or 1) = 00000001( (= 1)
    # ...
    # 239 (11101111) & (1 << 3) (= 00001000, or 8) = 00001000 (= 8)
    # 239 (11101111) & (1 << 4) (= 00010000, or 16) = 00000000 (found
    # that 239's binary pos 4 is 0!)

    for j in range(8):
      if b & (1 << j) == 0:
        # don't forget the bigger part i * 8
        return i * 8 + j

print(missingIntWith1G([0,1,3,4]))

# FOLLOW UP
# What if you have only 10 MB of memory? Assume that all the values are
# distinct and we now have no more than one billion non-negative
# integers.

def missingIntWith10M(ints):
  # First round:
  # devide ints into count buckets each holds the number of
  # int found in a particular int range. Each bucket should be able to
  # hold an integer counter (4 bytes). Altogether, the buckets should
  # cover the whole range of all non-negative 32 bit ints (0 ~ 2^31-1).
  # numAllDifferentInts / rangeSize * 4 bytes <= 10 MB <= 2^23 bytes
  # (10MB = 2^20 bytes * 10 > (2^20 bytes * 8 = 2^23 bytes))
  # => 2^31 / rangeSize <= 2^21
  # => rangeSize >= 2^31/2^21 = 2^10
  # Second round: 
  # when a range is found, in which counter < rangeSize, we need to
  # build a bit vector covering every integer in that range. Since we
  # use a byte array for the bit vector, each item is 1 byte = 8 bits
  # and can store the found/not found status for 8 integers. To make
  # sure the whole bit vector fits in 10MB memory:
  # bvArraySize = rangeSize / byteSize(8) <= 10MB = 2^23 bytes
  # => rangeSize <= 2^23 * 2^3 = 2^26
  # => 2^10 <= rangeSize <= 2^26
  # To minimize memory usage in both rounds, the most optimized rangeSize 
  # is the middle point of 2^10 and 2^26
  rangeSize = 2 ** ((10 + 26) // 2)
  rangeIdx = findMissingIntRangeIdx(ints, rangeSize)
  if rangeIdx != -1:
    return findMissingIntInRange(ints, rangeSize, rangeIdx)
  return -1

def findMissingIntRangeIdx(ints, rangeSize):
  INT_UPPER_BOUND = 2**21 - 1
  counterList = [0] * (INT_UPPER_BOUND // rangeSize + 1)
  for int in ints:
    counterPos = int // rangeSize
    counterList[counterPos] += 1
  for i in range(len(counterList)):
    if ((i != len(counterList) - 1 and counterList[i] < rangeSize) or 
      (i == len(counterList) - 1 and counterList[i] < INT_UPPER_BOUND % rangeSize)):
        return i
  return -1

def findMissingIntInRange(ints, rangeSize, rangeIdx):
  bvs = bytearray(rangeSize // 8 + 1)
  rangeLowerBound = rangeSize * rangeIdx
  rangeUpperBound = rangeLowerBound + rangeSize
  for int in ints:
    if int >= rangeLowerBound and int < rangeUpperBound:
      offset = int - rangeLowerBound
      bvs[offset // 8] |= (1 << (offset % 8))
  for i in range(len(bvs)):
    byte = bvs[i]
    for j in range(8):
      if byte & (1 << j) == 0:
        return i * 8 + j + rangeLowerBound
  return -1

print(missingIntWith10M([0,1,3,4]))