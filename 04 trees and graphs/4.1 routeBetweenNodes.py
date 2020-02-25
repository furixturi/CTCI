# Route Between Nodes: 
# Given a directed graph, design an algorithm to find out 
# whether there is a route between two nodes.

from collections import deque
def routeExist(adjacencyList, start, end):
  queue = deque()
  queue.append([start])
  while queue:
    subPath = queue.popleft()
    lastEnd = subPath[len(subPath)-1]
    for n in adjacencyList[lastEnd]:
      if n == end:
        return True
      if n not in subPath:
        queue.append(subPath + [n])
  return False
