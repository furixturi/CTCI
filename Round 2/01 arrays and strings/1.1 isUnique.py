# Is Unique: Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional data structures?
def isUnique(str):
  map = {}
  for c in str:
    if c in map:
      return False
    else: 
      map[c] = True
  return True

# ord('a') is 97
# chr(97) is 'a'
def isUniqueSol(str):
  tab = [False] * 128
  for c in str:
    ordC = ord(c)
    if tab[ordC]:
      return False
    else:
      tab[ordC] = True
  return True

print(isUnique('aab'))
print(isUnique('abc'))
print(isUniqueSol('abcdefghijklmn'))
print(isUniqueSol('aaabecslt'))