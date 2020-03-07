# Power Set: Write a method to return all subsets of a set.
import random
def allSubSets(s):
  if len(s) == 0:
    return [set()]
  item = random.choice(tuple(s))
  itemSet = set([item])
  lastSet = s.copy()
  lastSet.remove(item)
  allLastSubsets = allSubSets(lastSet)
  newSubsets = []
  for lastSubset in allLastSubsets:
    newSubsets.append(lastSubset | itemSet)
  return allLastSubsets + newSubsets

print(allSubSets(set([1,2,3])))