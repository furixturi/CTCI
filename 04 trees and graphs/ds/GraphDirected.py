from collections import deque

class DirectedGraph:
  def __init__(self, ajl = {}):
    self.ajl = ajl

  def topologicalSort(self):
    inboundEdgeCount = {}
    for v in self.ajl:
      inboundEdgeCount[v] = 0
    for v in self.ajl:
      for n in self.ajl[v]:
        inboundEdgeCount[n] += 1
    startVertices = [vertex for (vertex, count) in inboundEdgeCount.items() if count == 0]
    if not startVertices:
      raise Exception('Graph contains cycle.')
    # the result sorted
    order = deque()
    # deque can be generated from a list
    processNext = deque(startVertices)
    # deque will be False if empty
    while processNext:
      curr = processNext.popleft()
      for neighbor in self.ajl[curr]:                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        inboundEdgeCount[neighbor] -= 1
        if inboundEdgeCount[neighbor] == 0:
          processNext.append(neighbor)
      order.append(curr)
    return order

if __name__ == '__main__':
  ajl = {
    'A': ['B', 'F', 'H'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': [],
    'G': ['B'],
    'H': ['G']
  }

  g = DirectedGraph(ajl)
  print(list(g.topologicalSort()))
