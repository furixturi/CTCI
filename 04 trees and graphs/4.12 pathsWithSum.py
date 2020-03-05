# Paths with Sum: 
# You are given a binary tree in which each node contains an integer value 
# (which might be positive or negative). Design an algorithm to count the 
# number of paths that sum to a given value. The path does not need to start 
# or end at the root or a leaf, but it must go downwards (traveling only 
# from parent nodes to child nodes).

# brute-force 
# balanced binary tree time complexity O(NlogN)
# worst time complexity O(N^2) - tree height is N
def pathsWithSum(tree, targetSum):
  if tree is None:
    return 0

  # find number of paths starting from the root
  totalFromRoot = pathsThroughNode(tree, targetSum, 0)
  # recursively find number of paths starting from each node in the left
  # subtree
  totalOnTheLeft = pathsWithSum(tree.left, targetSum)
  # recursively find number of paths starting from each node in the
  # right subtree
  totalOnTheRight = pathsWithSum(tree.right, targetSum)

  return totalFromRoot + totalOnTheLeft + totalOnTheRight

def pathsThroughNode(node, targetSum, currentSum):
  if node is None:
    return 0
  totalThroughNode = 0
  
  # check if the path ending at current node satisfies targetSum
  currentSum += node.data
  if currentSum == targetSum:
    totalThroughNode += 1
  
  # check path ending at each node of the left subtree
  totalThroughNode += pathsThroughNode(node.left, targetSum, currentSum)
  # check path ending at each node of the right subtree
  totalThroughNode += pathsThroughNode(node.right, targetSum, currentSum)
  
  return totalThroughNode

# optimized with memoization
def pathsWithSum2(tree, targetSum, runningSum=0, pathCountMap={}):
  # base case
  if tree is None:
    return 0

  # Update runningSum with current node's data  
  runningSum += tree.data

  # check if current node is the end of a path from root
  totalPath = 0 if runningSum != targetSum else 1

  # check if current node is the end of a path from an ancestor node
  # other than the root
  preSum = runningSum - targetSum
  if preSum in pathCountMap:
    totalPath += pathCountMap[preSum]

  # add current node's runningSum to the countMap for its children to use
  if runningSum in pathCountMap:
    pathCountMap[runningSum] += 1
  else:
    pathCountMap[runningSum] = 1

  # check current node's children recursively
  totalPath += pathsWithSum2(tree.left, targetSum, runningSum, pathCountMap)
  totalPath += pathsWithSum2(tree.right, targetSum, runningSum, pathCountMap)
  
  # remove current node's runningSum from the countMap since it will be
  # given back to its parent call, which reuses the map in current
  # node's sibling (and the sibling's children), where the current node is not in that path
  pathCountMap[runningSum] -= 1

  return totalPath