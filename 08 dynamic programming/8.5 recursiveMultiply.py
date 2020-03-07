# Recursive Multiply: Write a recursive function to multiply two
# positive integers without using the *operator.You can use addition,
# subtraction, and bit shifting, but you should minimize the number of
# those operations.
def multiplyRecursive(a, b):
  if a == 0 or b == 0:
    return 0

  bigger = b if a < b else a
  smaller = a if a < b else b
  
  if smaller == 1:
    return bigger
  return multiplyRecursive(bigger, smaller-1) + bigger

print(multiplyRecursive(20,30))

def multiplyRecursiveSolution(a, b):
  bigger = b if a < b else a
  smaller = a if a < b else b
  if smaller == 0:
    return 0
  if smaller == 1:
    return bigger

  s = smaller >> 1 # equals to s // 2
  side1 = multiplyRecursiveSolution(s, bigger)
  side2 = side1 if smaller % 2 == 0 else side1 + bigger
  return side1 + side2
  
print(multiplyRecursiveSolution(25,32))

  