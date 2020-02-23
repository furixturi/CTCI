import math
class MinHeap:
  def __init__(self, items=[]):
    self.items = items

  def __repr__(self):
    return repr(self.items)

  def add(self, item):
    self.items.append(item)
    items = self.items
    currIdx = len(self.items) - 1
    parentIdx = math.ceil((currIdx - 2) / 2)
    while parentIdx >= 0 and item <= items[parentIdx]:
      items[currIdx], items[parentIdx] = items[parentIdx], items[currIdx]
      parentIdx = math.ceil((currIdx - 2) / 2)
      currIdx = parentIdx

  def extractMin(self):
    items = self.items
    items[0], items[len(items)-1] = items[len(items)-1], items[0]
    result = items.pop()
    currIdx = 0
    leftChildIdx = currIdx * 2 + 1
    rightChildIdx = currIdx * 2 + 2
    while leftChildIdx < len(items) and (
        items[leftChildIdx] < items[currIdx]  
        or (rightChildIdx < len(items) and items[rightChildIdx] < items[currIdx])
      ):
      smallerChildIdx = leftChildIdx if (
          rightChildIdx >= len(items) or 
          items[leftChildIdx] < items[rightChildIdx]
        ) else rightChildIdx
      items[currIdx], items[smallerChildIdx] = items[smallerChildIdx], items[currIdx]
      currIdx = smallerChildIdx
      leftChildIdx = currIdx * 2 + 1
      rightChildIdx = currIdx * 2 + 2
    return result

if __name__ == '__main__':
  heap = MinHeap([0,5,8,13])
  heap.add(2)
  heap.add(4)
  heap.add(9)
  print(heap)
  print(heap.extractMin())
  print(heap)