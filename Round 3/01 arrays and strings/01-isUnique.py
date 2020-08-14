# Is Unique: Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional data structures?

def isUnique(s):
  d = {}
  for c in s:
    if c in d:
      return False
    else:
      d[c] = True
  return True

def isUnique2(s):
  l = [False] * 128
  for c in s:
    i = ord(c)
    if l[i]:
      return False
    else:
      l[i] = True
  return True

if __name__ == '__main__':
  print(isUnique2('aaa'))
  print(isUnique2('abc'))