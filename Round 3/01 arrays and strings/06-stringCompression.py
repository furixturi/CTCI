# String Compression: Implement a method to perform basic string
# compression using the counts of repeated characters. For example, the
# string aabcccccaaa would become a2b1c5a3. If the "compressed" string
# would not become smaller than the original string, your method should
# return the original string. You can assume the string has only
# uppercase and lowercase letters (a - z).
def stringCompression(s):
  if len(s) <= 2: return s
  curr = s[0]
  currCount = 1
  res = [s[0]]

  for i in range(1, len(s)):
    c = s[i]
    if c == curr:
      currCount += 1
    else:
      res.append(str(currCount))
      res.append(c)
      currCount = 1
      curr = c
    if i+1 >= len(s):
      res.append(str(currCount))

  sres = ''.join(res)
  return s if len(s) <= len(sres) else sres

if __name__ == '__main__':
  print(stringCompression('aabcccccaaa'))
  print(stringCompression('aabbccccd'))
  print(stringCompression('aabcc'))
  print(stringCompression('a'))