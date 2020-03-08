# Permutations without Dups: Write a method to compute all permutations
# of a string of unique characters.
# O(n^2 * n!)

def perms(s):
  if len(s) <= 1:
    return [s]
  lastPerms = perms(s[0:len(s)-1]) # O(n) recursive calls of O(n!) * O(n) work
  c = s[len(s)-1]
  newPerms = []
  for perm in lastPerms: # O(n!)
    for i in range(len(perm) + 1): # O(n)
      newPerm = perm[0:i] + c + perm[i:]
      newPerms.append(newPerm)
  return newPerms

print(perms(''))
print(perms('a'))
print(perms('ab'))
print(perms('abc'))