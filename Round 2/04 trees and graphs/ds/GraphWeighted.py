class Node:
  def __init__(self, label, data):
    self.label = label
    self.data = data

class MinHeap:
  def __init__(self, items = []):
    self.items = []
    for item in items:
      self.insert(item)

  def __str__(self):
    return str(self.items)

  def isEmpty(self):
    return len(self.items) == 0

  def insert(self, item):
    self.items.append(item)
    idx = len(self.items) - 1
    self.bubbleUp(idx)

  def extractMin(self):
    return self.extractAt(0)

  def extractAt(self, idx = 0):
    item = self.items[idx]
    self.items[idx] = self.items.pop()
    self.bubbleDown(idx)
    return item

  def updateItem(self, label, newData):
    targetIdx, targetItem = self.findByLabel(label)
    if targetIdx == -1:
      print(f'{label} does not exist')
      return    
    targetItem.data = newData
    self.adjustItemPosition(targetIdx)

  def findByLabel(self, label):
    targetIdx = -1
    targetItem = None
    for idx, item in enumerate(self.items):
      if item.label == label:
        targetIdx = idx
        targetItem = item
    if targetIdx == -1:
      print(f'{label} is not in the MinHeap')
    return (targetIdx, targetItem)

  def adjustItemPosition(self, idx = -1):
    if idx < 0 or idx >= len(self.items):
      return
    self.bubbleUp(idx)
    self.bubbleDown(idx)

  def bubbleUp(self, startIdx = -1):
    if startIdx < 0 or startIdx >= len(self.items):
      return
    idx = startIdx
    parentIdx = (idx + 1) // 2 - 1
    while parentIdx >= 0 and self.items[parentIdx].data > self.items[idx].data:
      self.items[parentIdx], self.items[idx] = self.items[idx], self.items[parentIdx]
      idx = parentIdx
      parentIdx = (idx + 1) // 2 - 1

  def bubbleDown(self, startIdx = 0):
    if startIdx < 0 or startIdx >= len(self.items):
      return
    idx = startIdx
    leftChildIdx = 2 * idx + 1
    rightChildIdx = 2 * idx + 2
    while idx < len(self.items) and (
        leftChildIdx < len(self.items) and self.items[leftChildIdx].data < self.items[idx].data or (
          rightChildIdx < len(self.items) and self.items[rightChildIdx].data < self.items[idx].data
        )
      ):
      smallerChildIdx = rightChildIdx if (rightChildIdx < len(self.items) and 
        self.items[rightChildIdx].data < self.items[leftChildIdx].data) else leftChildIdx
      self.items[idx], self.items[smallerChildIdx] = self.items[smallerChildIdx], self.items[idx]
      idx = smallerChildIdx
      leftChildIdx = 2 * idx + 1
      rightChildIdx = 2 * idx + 2

class GraphDirectedWeighted:
  def __init__(self, ajl = {}):
    self.ajl = ajl

  def addVertex(self, v):
    if v in self.ajl:
      print(f'{v} is already in the graph')
  
  def addEdge(self, v1, v2, weight, bidirectional = False):
    self.ajl[v1][v2] = weight
    if bidirectional:
      self.ajl[v2][v1] = weight
  
  def removeVertex(self, v):
    if not v in self.ajl:
      print(f'{v} is not in the graph')
      return
    for vertex in self.ajl:
      if vertex != v:
        if v in self.ajl[vertex]:
          del self.ajl[vertex][v]
      else:
        del self.ajl[vertex]
  
  def removeEdge(self, v1, v2, bidirectional = False):
    if v1 not in self.ajl:
      print(f'{v1} is not in the graph')
      return
    if v2 not in self.ajl:
      print(f'{v2} is not in the graph')
      return
    if v2 in self.ajl[v1]:
      del self.ajl[v1][v2]
    else:
      print(f'There is no edge from {v1} to {v2}')
    if bidirectional:
      if v1 in self.ajl[v2]:
        del self.ajl[v2][v1]
      else:
        print(f'There is no edge from {v1} to {v1}')
  
  def dijkstra(self, startVertex):
    if not startVertex in self.ajl:
      print(f'{startVertex} is not in the graph')
      return None
    remaining = MinHeap()
    shortestPathWeight = {}
    prevNodes = {}
    for v in self.ajl:
      if v == startVertex:
        remaining.insert(Node(v, 0))
        shortestPathWeight[v] = 0
        prevNodes[v] = v
      else:
        remaining.insert(Node(v, float("inf")))
        shortestPathWeight[v] = float("inf")
        prevNodes[v] = None
    while not remaining.isEmpty():
      curr = remaining.extractMin()
      for n in self.ajl[curr]:
        pathWeight = shortestPathWeight[curr] + self.ajl[curr][n]
        if pathWeight < shortestPathWeight[n]:
          shortestPathWeight[n] = pathWeight
          remaining.updateItem(n, shortestPathWeight)
          prevNodes[n] = curr
    return prevNodes
