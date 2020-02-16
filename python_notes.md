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

