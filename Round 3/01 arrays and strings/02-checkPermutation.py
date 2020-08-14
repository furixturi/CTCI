# Check Permutation: Given two strings,write a method to decide if one
# is a permutation of the other.

# check char count with ascii list
def checkPerm(s1, s2):
  if len(s1) != len(s2):
    return False
  t = [0] * 128
  for c in s1:
    i = ord(c)
    t[i] += 1
  for c in s2:
    i = ord(c)
    t[i] -= 1
  for n in t:
     if n != 0:
       return False
  return True

# check char count with a dict
def checkPerm2(s1, s2):
  if len(s1) != len(s2):
    return False
  d = {}
  for c in s1:
    if c in d:
      d[c] += 1
    else:
      d[c] = 1
  for c in s2:
    if c in d:
      d[c] -= 1
    else:
      return False
  for k in d:
    if d[k] != 0:
      return False
  return True

# compare sorted string
def checkPerm3(s1, s2):
  ss1 = sorted(s1)
  ss2 = sorted(s2)
  return ss1 == ss2

if __name__ == '__main__':
  print(checkPerm('abc', 'abc'))
  print(checkPerm('abc', 'cba'))
  print(checkPerm('abc', 'cca'))
  print(checkPerm2('abc', 'abc'))
  print(checkPerm2('abc', 'cba'))
  print(checkPerm2('abc', 'cca'))
  print(checkPerm3('a c', 'ac'))