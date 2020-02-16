# One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, pales -> true pales, pale -> true pale, bale -> true pale, bake ->
# false
# time complexity O(n), n is the length of the shorter string

def oneWay(src: str, comp: str):
  if abs(len(src) - len(comp)) > 1:
    return False
  # replace case
  if len(src) == len(comp):
    num_diff = 0
    for i, c in enumerate(src):
      if src[i] != comp[i]:
        if num_diff == 0:
          num_diff += 1
        else:
          return False
  # insert or remove case
  else:
    if len(src) - len(comp) == 1:
      short = comp
      long = src
    else:
      short = src
      long = comp
    i = 0
    j = 0
    while i < len(short) and j < len(long):
      num_diff = 0
      if short[i] != long[j]:
        if num_diff > 0:
          return False
        j += 1
        num_diff += 1
      else:
        i += 1
        j += 1
  return True

print(oneWay('pale', 'pales')) # True
print(oneWay('pale', 'ple')) # True
print(oneWay('pale', 'bale')) # True
print(oneWay('pale', 'bake')) # False
