# Permutations with Dups: Write a method to compute all permutations of
# a string whose charac­ters are not necessarily unique. The list of
# permutations should not have duplicates.
import time
def permWithDups(s):
  if len(s) == 0:
    return ['']
  
  result = []
  checked = set()
  for i in range(len(s)):
    c = s[i]
    if c not in checked:
      checked.add(c)
      pre = s[0:i]
      post = s[i+1:]
      lastPerms = permWithDups(pre + post)
      for lastPerm in lastPerms:
        result.append(c + lastPerm)
  return result

def permWithDupsOptimize(s):
  cMap = {}
  for c in s:
    if c in cMap:
      cMap[c] += 1
    else:
      cMap[c] = 1
  result = []
  addPerm('', cMap, len(s), result)
  return result

def addPerm(prefix, cMap, slotsToFill, result):
  if slotsToFill == 0:
    result.append(prefix)
    return
  for c in cMap:
    if cMap[c] > 0:
      cMap[c] -= 1
      addPerm(prefix + c, cMap, slotsToFill - 1, result)
      cMap[c] += 1

def permWithDupsSolution(s):
  cCount = {}
  for c in s:
    if c not in cCount:
      cCount[c] = 1
    else:
      cCount[c] += 1
  result = []
  permHelper(cCount, '', len(s), result)
  return result

def permHelper(cMap, prefix, remaining, result):
  if remaining == 0:
    result.append(prefix)
    return
  
  for c in cMap:
    if cMap[c] > 0:
      cMap[c] -= 1
      permHelper(cMap, prefix + c, remaining - 1, result)
      cMap[c] += 1



print(permWithDups('aaa'))

start = time.process_time()
permWithDups('aabaabaabbb')
end = time.process_time()
print(end - start)

start = time.process_time()
permWithDupsSolution('aabaabaabbb')
end = time.process_time()
print(end - start)