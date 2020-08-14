# One Away: There are three types of edits that can be performed on
# strings: insert a character, remove a character, or replace a
# character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
def oneAway(s1, s2):
  lenDiff = abs(len(s1)-len(s2))
  if lenDiff == 0:
    return oneReplaceAway(s1, s2)
  elif lenDiff == 1:
    ss = s1 if len(s1) < len(s2) else s2
    sl = s1 if len(s2) < len(s1) else s2
    return oneInsertAway(ss, sl)
  return False

def oneReplaceAway(s1, s2):
  diff = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      if diff > 0:
        return False
      else:
        diff = 1
  return True

def oneInsertAway(ss, sl):
  i1 = 0
  i2 = 0
  while i2 < len(sl):
    if ss[i1] != sl[i2]:
      i2 += 1
    if ss[i1] != sl[i2]:
      return False
    i1 += 1
    i2 += 1
  return True

if __name__ == '__main__':
  print(oneAway('aple', 'apple'))
  print(oneAway('pale', 'ple'))
  print(oneAway('pale', 'bae'))
  print(oneAway('apple', 'appde'))