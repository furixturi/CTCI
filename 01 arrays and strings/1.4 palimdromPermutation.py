# Palindrome Permutation: Given a string, write a function to check if 
# it is a permutation of a palin­drome. A palindrome is a word or phrase 
# that is the same forwards and backwards. A permutation is a rearrangement 
# of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

def isPalindromePermutation(str: str) -> bool:
  str = ''.join(str.lower().split(' '))
  if len(str) <= 1:
    return True
  dict = {}
  for c in str:
    if c in dict:
      dict[c] -= 1
    else:
      dict[c] = 1
  count = 0
  for c in dict:
    count += dict[c]
  return count < 2

print(isPalindromePermutation('Tact Coa'))