# Parens: Implement an algorithm to print all valid (e.g., properly opened 
# and closed) combinations of n pairs of parentheses.
# EXAMPLE
# Input: 3
# Output: ((())), (()()), (())(), ()(()), ()()()

def parens(numPairs):
  parenMap = {
    '(': numPairs,
    ')': numPairs
  }
  result = []
  addParen('', parenMap, result)
  return result

def addParen(prefix, parenMap, result):
  if parenMap['('] == 0 and parenMap[')'] == 0:
    result.append(prefix)
    return
  
  if parenMap['('] > 0:
    parenMap['('] -= 1
    addParen(prefix + '(', parenMap, result)
    parenMap['('] += 1
  if parenMap[')'] > 0 and parenMap[')'] > parenMap['(']:
    parenMap[')'] -= 1
    addParen(prefix + ')', parenMap, result)
    parenMap[')'] += 1

def parensSolution(numPairs):
  result = []
  addParenSolution(result, numPairs, numPairs, '')
  return result

def addParenSolution(result, leftRemain, rightRemain, prefix):
  if leftRemain == 0 and rightRemain == 0:
    result.append(prefix)
    return
  if leftRemain < 0 or rightRemain < leftRemain:
    return
  newPrefix = prefix + '('
  addParenSolution(result, leftRemain-1, rightRemain, newPrefix)
  newPrefix = prefix + ')'
  addParenSolution(result, leftRemain, rightRemain-1, newPrefix)


print(parens(3))
print(parensSolution(3))