# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold 
# the additional characters,and that you are given the "true" length of 
# the string. (Note: If implementing in Java, please use a character array
# so that you can perform this operation in place.)

def urlify(s, length):
  # s = s.strip()
  # l = []
  # for c in s: 
  #   if c == ' ':
  #     l.append('%20')
  #   else:
  #     l.append(c)
  return '%20'.join(s.strip().split(' '))

if __name__ == '__main__':
  print(urlify('Mr John Smith ', 13))