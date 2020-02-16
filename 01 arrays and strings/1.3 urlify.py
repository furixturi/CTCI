# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold 
# the additional characters,and that you are given the "true" length of 
# the string. (Note: If implementing in Java, please use a character array 
# so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"

def urlify(str: str, len: int) -> None:
  # return  str.strip().replace(' ', '20%')
  return '20%'.join(str.strip().split(' ')) # Python join is a string method on the delimiter!

print(urlify('Mr John  Smith ', 13))