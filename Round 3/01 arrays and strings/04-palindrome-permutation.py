# Palindrome Permutation: Given a string, write a function to check if
# it is a permutation of a palin­drome. A palindrome is a word or
# phrase that is the same forwards and backwards. A permutation is a
# rearrangement of letters. The palindrome does not need to be limited
# to just dictionary words.

def palindromePermutaion(s):
  length = 0
  d = {}
  for c in s:
    if c != ' ':
      c = c.lower()
      length += 1
      if c not in d:
        d[c] = 1
      else:
        del d[c]
  count = 0
  for c in d:
    count += d[c]
  return (length % 2 == 0 and count == 0) or (length % 2 == 1 and count == 1)

if __name__ == '__main__':
  print(palindromePermutaion('Tact Coa'))
  print(palindromePermutaion('aaaaa'))
