# Is Unique: Implement an algorithm to determine if a string has all 
# unique characters. What if you cannot use additional data structures?

def isUnique(string: str) -> bool:
  map = {}
  for char in string:
    if char in map:
      return False
    map[char] = True
  return True

# Solution: 
# - Ask if it is an ASCII string, if yes, use an array indexed by char code
def isUniqueSolution(string: str) -> bool:
  if len(string) > 128: # 256 https://www.ascii-code.com/
    return False
  char_set = [False]*128
  for char in string:
    if char_set[ord(char)] == True: # ord(char) get the char code from a char, 
                                    # chr(num) gets the char from a char code
      return False
    char_set[ord(char)] = True
  return True

print(isUniqueSolution('fine'))
print(isUniqueSolution('hello'))
print(isUniqueSolution(''))