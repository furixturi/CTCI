# String Rotation: Assume you have a method isSubstring which checks if one
# word is a substring of another. Given two strings, sl and s2, write
# code to check if s2 is a rotation of sl using only one call to
# isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").

def isSubstring(substring, string):
  return substring in string

def isRotatedString(s1, s2):
  if len(s1) != len(s2): return False
  return isSubstring(s1, s2*2)

if __name__ == '__main__':
  print(isRotatedString('abcd', 'cdab'))
  print(isRotatedString('abcd', 'cdcd'))
  print(isRotatedString('', 'cdcd'))
  print(isRotatedString('', ''))