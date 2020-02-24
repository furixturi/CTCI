
class Trie:
  def __init__(self, char = 'root', prefix = ''):
    self.char = char
    self.prefix = prefix
    self.children = {}

  def __repr__(self):
    return f'{self.char}'

  def __str__(self, level=0):
    result = '  ' * (level - 1) if level >=1 else ''
    result += '|-' if level >= 1 else ''
    result += repr(self) + '\n'
    for c in self.children:
      child = self.children[c]
      result += child.__str__(level + 1)
    return result
    
  def addWord(self, word):
    if word == '':
      word ='*'
    char = word[0]
    if char in self.children:
      child = self.children[char]
    else:
      child = Trie(char, self.prefix + char)
      self.children[char] = child
      if word == '*':
        return
    child.addWord(word[1:])

if __name__ == '__main__':
  trie = Trie()
  trie.addWord('MANY')
  trie.addWord('MY')
  trie.addWord('MAN')
  trie.addWord('LIE')
  trie.addWord('A')
  print(trie)
