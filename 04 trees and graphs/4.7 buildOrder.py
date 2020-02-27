# Build Order: 
# You are given a list of projects and a list of dependencies (which is a 
# list of pairs of projects, where the second project is dependent on the 
# first project). All of a project's dependencies must be built before the 
# project is. Find a build order that will allow the projects to be built. 
# If there is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) Output: f, e, a,
# b, d, c

def buildOrder(projects, dependencies):
  depRelation = {}
  depCount = {}
  order = []
  for project in projects:
    depRelation[project] = []
    depCount[project] = 0
  for dep in dependencies:
    depRelation[dep[0]].append(dep[1])
    depCount[dep[1]] += 1
  while depCount:
    noDependencyProjects = [key for key, val in depCount.items() if val == 0]
    if len(noDependencyProjects) == 0:
      raise Exception('All projects have dependencies, cannot start any of them')
    for p in noDependencyProjects:
      del depCount[p]
      order.append(p)
      for dp in depRelation[p]:
        depCount[dp] -= 1
  return order