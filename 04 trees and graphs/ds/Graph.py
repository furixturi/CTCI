from queue import Queue
class Vertex:
  def __init__(self, key, data):
    if key == None:
      raise ValueError('Vertex key is required.')
    self.key = key
    if data == None:
      data = key
    self.data = data

  def __repr__(self):
    return f'{{ key: {repr(self.key)}, data: {repr(self.data)} }}'

class Graph:
  def __init__(self):
    self.adjacencyList = {}
  
  def __repr__(self):
    result = ''
    for vertex, edges in self.adjacencyList.items():
      result += f'{vertex} : {edges}\n'
    return result

  def addVertex(self, vertex):
    if vertex in self.adjacencyList:
      raise ValueError(f'Vertex {str(vertex)} already exists.')
    self.adjacencyList[vertex] = []

  def addEdge(self, v1, v2):
    if v1 not in self.adjacencyList or v2 not in self.adjacencyList:
      notExistVertex = v1 if v1 not in self.adjacencyList else v2
      raise ValueError(f'Vertex {str(notExistVertex)} is not in the graph.')
    self.adjacencyList[v1].append(v2)
    self.adjacencyList[v2].append(v1)

  def removeEdge(self, v1, v2):
    if v1 not in self.adjacencyList or v2 not in self.adjacencyList:
      notExistVertex = v1 if v1 not in self.adjacencyList else v2
      raise ValueError("{} does not exist in the graph".format(notExistVertex))
    if v1 not in self.adjacencyList[v2]:
      raise ValueError(f'No edge between {v1} and {v2}. Cannot remove.')
    self.adjacencyList[v1].remove(v2)
    self.adjacencyList[v2].remove(v1)

  def removeVertex(self, vertex):
    if vertex not in self.adjacencyList:
      raise ValueError(f'{vertex} is not in the graph. Cannot remove.')
    edges = self.adjacencyList[vertex]
    for v in edges:
      self.removeEdge(vertex, v)
    del self.adjacencyList[vertex]
    
  def dfs_preOrder(self, startVertex, pastNodes = set()):
    if startVertex not in self.adjacencyList:
      raise ValueError(f'Vertex {startVertex} is not found in the graph')
    pastNodes.add(startVertex)
    print(startVertex)
    for neighbor in self.adjacencyList[startVertex]:
      if neighbor not in pastNodes:
        self.dfs_preOrder(neighbor, pastNodes)

  def dfs_postOrder(self, startVertex, pastNodes = set()):
    if startVertex not in self.adjacencyList:
      raise ValueError(f'{startVertex} is not in the graph.')
    pastNodes.add(startVertex)
    for neighbor in self.adjacencyList[startVertex]:
      if neighbor not in pastNodes:
        self.dfs_postOrder(neighbor, pastNodes)
    print(startVertex)

  def bfs(self, startVertex, targetVertexKey = None):
    if startVertex not in self.adjacencyList:
      raise ValueError(f'{startVertex} is not in the graph.')
    queue = [startVertex]
    pastNodes = set()
    while len(queue) > 0:
      v = queue.pop(0)
      if v.key == targetVertexKey:
        return v
      pastNodes.add(v)
      for neighbor in self.adjacencyList[v]:
        if neighbor not in pastNodes and neighbor not in queue:
          queue.append(neighbor)
      if targetVertexKey == None:
        print(v)

  def findAPath(self, start, end):
    if start == end:
      return [start]
    queue = Queue(len(self.adjacencyList.keys()))
    pastVertices = set()
    queue.put([start])
    # path = [start]
    while not queue.empty():
      currPath = queue.get()
      curr = currPath[len(currPath) - 1]
      pastVertices.add(curr)
      for neighbor in self.adjacencyList[curr]:
        if neighbor == end:
            return currPath + [neighbor]
        if neighbor not in pastVertices:
          queue.put(currPath + [neighbor])
    return None

  def findAllPaths(self, start, end):
    if start == end:
      return [[start]]
    queue = Queue(0)
    paths = []
    queue.put([start])
    while not queue.empty():
      currPath = queue.get()
      curr = currPath[len(currPath) - 1]
      for neighbor in self.adjacencyList[curr]:
        if neighbor not in currPath:
          if neighbor == end:
            paths.append(currPath + [neighbor])
          else:
            queue.put(currPath + [neighbor])
    return paths

    
  
if __name__ == '__main__':
  g = Graph()
  vertices = []
  for i in range(5):
    v = Vertex(i, i+1)
    vertices.append(v)
    g.addVertex(v)
  g.addEdge(vertices[0], vertices[1])
  g.addEdge(vertices[1], vertices[2])
  g.addEdge(vertices[2], vertices[3])
  g.addEdge(vertices[3], vertices[4])
  g.addEdge(vertices[4], vertices[0])
  g.addEdge(vertices[4], vertices[1])
  g.addEdge(vertices[3], vertices[0])
  print(g)
  # g.removeEdge(vertices[3], vertices[0])
  # print(g)
  # g.removeEdge(vertices[3], vertices[0])
  # g.removeVertex(vertices[0])
  # print(g)
  print('=== pre order ===')
  g.dfs_preOrder(vertices[1])
  print('=== post order ===')
  g.dfs_postOrder(vertices[1])
  print('=== bfs ===')
  g.bfs(vertices[1])
  print('=== bfs search key == 2 ===')
  print(g.bfs(vertices[1], 2))
  print(f'=== find a path between {vertices[1]} and {vertices[3]}')
  print(g.findAPath(vertices[1], vertices[3]))
  print(f'=== find all paths between {vertices[1]} and {vertices[3]}')
  print(g.findAllPaths(vertices[1], vertices[3]))