# Group Anagrams: Write a method to sort an array of strings so that all
# the anagrams are next to each other.
def sortAnagram(stringList):
  anagramMap = {}
  for s in stringList:
    charCoumtMap = {}
    for c in s:
      charCoumtMap[c] = 1 if c not in charCoumtMap else charCoumtMap[c]+1
    t = tuple(charCoumtMap)
    if t in anagramMap:
      anagramMap[t].append(s)
    else:
      anagramMap[t] = [s]
  i = 0
  for t in anagramMap:
    anagramList = anagramMap[t]
    for a in anagramList:
      stringList[i] = a
      i += 1


def sortAnagramSolution(sl):
  sl.sort(key=lambda s: ''.join(sorted(s))) 

sl = ['ababa', 'max', 'cbc', 'babaa', 'bcc', 'cbb']
sortAnagramSolution(sl)
print(sl)