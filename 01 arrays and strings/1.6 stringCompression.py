# String Compression: 
# Implement a method to perform basic string compression using the counts 
# of repeated characters. For example, the string aabcccccaaa would become 
# a2b1c5a3. If the "compressed" string would not become smaller than the 
# original string, your method should return
# the original string. You can assume the string has only uppercase and 
# lowercase letters (a - z).

def stringCompression(string: str) -> str:
  result_list = []
  curr = None
  count = 0
  for i,c in enumerate(string):
    if c != curr:
      if count > 0:
        result_list.append(str(count))
      curr = c
      count = 1
      result_list.append(c)
    else:
      count += 1
    if i == len(string) -1:
      result_list.append(str(count))
  if len(result_list) >= len(string):
    result = string
  else:
    result = ''.join(result_list)
  return result

print(stringCompression('aabcccccaaa')) # 'a2b1c5a3'
print(stringCompression('')) # ''
print(stringCompression('abc')) # 'abc'