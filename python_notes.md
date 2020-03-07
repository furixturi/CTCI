# Add type hint for non-primitive built-in types

```python
from typing import List
```
# Generic type notation

```python
from typing import TypeVar
T = TypeVar('T')
# then you can do
items: List[T] = []
```
# Don't run scripts when imported as a module

```python
# what you want to import
class MyClass:
  ...

# what you only want to run when running directly this python file
if __name__ == '__main__':
  # do them here
```
# Reference a type in the class that defines it

After Python 3.6
```python
# must be at the top of the script file
from __future__ import annotations
```
# Return multiple values

Python functions can return multiple values, generally the same as Golang
```python
# return a tuple
def get_head(self) -> (T, LinkedListNode):
  data = self.data
  self = self.next
  return data, self

# use _ to ignore one of the returned value
_, new_list = old_list.get_head()
```
# Multiple possible types

Use a Union type
```python
from typing import Union
def return_int_or_None(happy: bool) -> Union[int, None]:
  if happy:
    return 42
  return None
```
# Stringify (how to print) instances of your class 

Implement __repr__() in your class. The repr() function calls it, and if
there is no __str__() method implemented, the print(), str(), format()
function also fallback to call it. So let it return a string, and you
can skip implementing the other

[official doc](https://docs.python.org/3.8/reference/datamodel.html?highlight=__repr__#object.__repr__)

```python
class MyClass:
  def __init__(self, data):
    self.data = data
  def __repr__(self) -> str:
    return str(self.data)
    return str(data)
```

# Infinity constant

## Positive

```python
import math
p_inf = math.inf # same as p_inf = float("+inf"), a tiny bit faster
p_inf > 9999999999999999999 # True
math.isinf(p_inf) and p_inf > 0 # True same as p_inf == float("+inf")
```

## Negative
```python
import math
n_inf = -math.inf
math.isinf(n_inf) # Also True
math.isinf(n_inf) and n_inf < 0 # Right way to check negative inf
```

# Use min() max() on iterable

min() returns the min value by default.
key= arg can receive a custom comparison function(lambda)

## List, tuple

```python
strs = ['hi', 'this', 'is', 'a', 'veryverylongword']
longestWord = max(strs, key = lambda x: len(x))
shortestWord = min(strs, key = lambda x: len(x))
# to get the index, use index(min(strs, ...))
```

## Dict

Strategy: Turn it to a list first

```python
myDict = {
  'a': 21,
  'b': 42,
  'c': 65536,
  'd': 65536
}

# the first key value pair with the max value
maxKeyValuePair = max(myDict.items(), key = lambda x: x[1]) # ('c', 65536)
keyOfMaxValue = maxKeyValuePair[0]
maxValue maxKeyValuePair[1]
```

# Dict

## Find key by value

```python
keys = [key for key, val in myDict.items() if val == 65536] # ['c', 'd']
```

# Check if key in dict

```python
if key in theDict:
```

# Check index exists list

```python
if i < len(theList):
```

# Get item index in list

```python
if item in theList:
  index = theList.index(item)
```

# randomly choose an item

## from a list

```python
import random
randomItem = random.choice(aList) # returns the value
```

## from a dict

```python
import random
randomKey = random.choice(list(aDict))
randomValue = aDict[randomKey]
```

## from a set

```python
import random
randomItem = random.choice(tuple(aSet)) # returns the set item
```