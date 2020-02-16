# String Rotation:
# Assume you have a method isSubstring which checks if one word is 
# a substring of another. Given two strings, sl and s2, write code 
# to check if s2 is a rotation of s1 using only one call to isSubstring 
# (e.g.,"waterbottle" is a rotation of "erbottlewat").

def isSubstring(s1: str, s2: str): 
  return s1.find(s2) != -1

# xy - rotate -> yx
# xy + xy = xyxy, yx is a substring
def isRotation(s1: str, s2: str) -> bool:
  return isSubstring(s1+s1, s2)

print(isRotation('waterbottle', 'erbottlewat'))