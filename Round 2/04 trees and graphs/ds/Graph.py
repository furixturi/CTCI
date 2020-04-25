# undirectional, unweighted graph
class Graph:
  def __init__(self):
    self.adjacencyList = {}

  def __repr__(self):
    return str(self.adjacencyList)

  def addVertex(self, v):
    if v in self.adjacencyList:
      print(f'{str(v)} already exists.')
    else:
      self.adjacencyList[v] = []
  
  def removeVertex(self, v):
    if v in self.adjacencyList:
      edges = self.adjacencyList[v]
      for v2 in edges:
        self.adjacencyList[v2].remove(v)
      del self.adjacencyList[v]

  def addEdge(self, v1, v2):
    if v1 not in self.adjacencyList:
      self.addVertex(v1)
    if v2 not in self.adjacencyList:
      self.addVertex(v2)
    self.adjacencyList[v1].append(v2)
    self.adjacencyList[v2].append(v1)

  def removeEdge(self, v1, v2):
    if not self.adjacencyList[v1]:
      print(f'{v1} is not in the graph')
      return
    if not self.adjacencyList[v2]:
      print(f'{v2} is not in the graph')
      return
    if v1 in self.adjacencyList[v2]:
      self.adjacencyList[v2].remove(v1)
    if v2 in self.adjacencyList[v1]:
      self.adjacencyList[v1].remove(v1)
  


  