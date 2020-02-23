import math
class WeightedGraph:
  def __init__(self, adjacencyList = {}):
    self.adjacencyList = adjacencyList

  def addVertex(self, vertex):
    if vertex in self.adjacencyList:
      raise ValueError(f'{vertex} already exist in graph')
    self.adjacencyList[vertex] = {}

  def addEdge(self, v1, v2, weight):
    if v1 not in self.adjacencyList or v2 not in self.adjacencyList:
      raise ValueError(f'One or more of the vertices are not in the graph.')
    self.adjacencyList[v1][v2] = weight
    self.adjacencyList[v2][v1] = weight

  def removeEdge(self, v1, v2):
    if v1 not in self.adjacencyList or v2 not in self.adjacencyList:
      raise ValueError(f'One or more of the vertices are not in the graph.')
    try:
      del self.adjacencyList[v1][v2]
    except KeyError:
      raise KeyError(f'edge does not exist')
    try:
      del self.adjacencyList[v2][v1]
    except KeyError:
      raise KeyError(f'edge does not exist')

  def removeVertex(self, v):
    for neighbor in self.adjacencyList[v]:
      self.removeEdge(v, neighbor)
    del self.adjacencyList[v]

  def Dijkstra(self, start):
    remaining = {}
    previous = {}
    pathWeights = {}
    # 1. Initialize remaining dict and pathWeights dict the same way:
    #   start vertex: 0
    #   other vertices: infinity
    #  Initialize the previous dict:
    #   start vertex: start vertex
    #   other vertices: None as not known yet
    for v in self.adjacencyList:
      if v == start:
        pathWeights[v] = 0
        remaining[v] = 0
        previous[v] = v
      else:
        pathWeights[v] = math.inf
        remaining[v] = math.inf
        previous[v] = None
    # 2. While the remaining is not drained
    #     [use bool() to check if a dict is empty]
    while bool(remaining):
      # 2.1 Take the vertex(curr) whose pathWeight is currently the smallest from remaining 
      # 2.2 Look each of its neighbors:
      # If curr's pathWeight + edgeWeight to the neighbor < than
      # neighbor's pathWeight:
      # 2.2.1 Update the neighbor's pathWeight to be curr's pathWeight +
      # edgeWeight in both remaining dict and pathWeights dict
      # 2.2.2 Update the neighbor's previous vertex to be curr
      #     [items() turns a dict to a list of (key, value) tuples]
      #     ["key" arg takes a lambda's returned value for comparison]
      #     [min()'s return value is the (key, value) tuple]
      #     [1. find the vertex with smallest pathWeight]
      curr = min(remaining.items(), key = lambda x: x[1])[0]
      del remaining[curr]
      for neighbor in self.adjacencyList[curr]:
        edgeWeight = self.adjacencyList[curr][neighbor]
        if edgeWeight + pathWeights[curr] < pathWeights[neighbor]:
          pathWeights[neighbor] = edgeWeight + pathWeights[curr]
          remaining[neighbor] = edgeWeight + pathWeights[curr]
          previous[neighbor] = curr
    return previous




if __name__ == '__main__':
  ajl = {
    'a': { 'b': 1, 'c': 5, 'd': 12 },
    'b': { 'a': 1, 'd': 3, 'g': 12, 'h': 9 },
    'c': { 'a': 5, 'd': 1, 'f': 2 },
    'd': { 'a': 12, 'b': 3, 'c': 1, 'e': 4, 'g': 1 },
    'e': { 'd': 4, 'i': 1 },
    'f': { 'c': 2, 'h': 1 },
    'g': { 'b': 12, 'd': 1 },
    'h': { 'b': 9, 'f': 1 },
    'i': { 'e': 1 }
  }
  g = WeightedGraph(ajl)
  print(g.Dijkstra('a'))