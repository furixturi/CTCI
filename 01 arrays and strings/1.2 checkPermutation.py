# Check Permutation: Given two strings,write a method to decide 
# if one is a permutation of the other.
# Permutation: same characters in different orders

# Count characters
def isPermutation(str1: str, str2: str) -> bool:
  if len(str1) != len(str2): 
    return False
  isSame = True
  dict1 = {}
  dict2 = {}
  for i, char1 in enumerate(str1):
    if char1 in dict1:
      dict1[char1] += 1
    else:
      dict1[char1] = 1
    char2 = str2[i]
    if char2 in dict2:
      dict2[char2] += 1
    else:
      dict2[char2] = 1
    if char1 != char2:
      isSame = False
  # completely the same, not a permutation
  if isSame:
    return False
  # check if a permutation
  for char in dict1:
    if char not in dict2 or dict1[char] != dict2[char]:
      return False
  return True

# Solutions
# - Ask if case sensitive
# - Ask if white space is significant
### Solution 1 sort the strings ###
def isPermutationSolution1(str1: str, str2: str) -> bool:
  if len(str1) != len(str2):
    return False
  return ''.join(sorted(str1)) == ''.join(sorted(str2))
### Solution 2 count characters ###
def isPermutationSolution2(str1: str, str2: str) -> bool:
  if len(str1) != len(str2):
    return False
  char_set = [0] * 128 # assumption
  for char1 in str1:
    char_set[ord(char1)] += 1
  for char2 in str2:
    char_set[ord(char2)] -= 1
    if char_set[ord(char2)] < 0:
      return False
  return True

print(isPermutationSolution2('', 'a'))
print(isPermutationSolution2('abc', 'abc'))
print(isPermutationSolution2('abc', 'acb'))