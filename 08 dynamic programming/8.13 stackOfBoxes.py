# Stack of Boxes: You have a stack of n boxes, with widths wi, heights
# hi, and depths di. The boxes cannot be rotated and can only be stacked
# on top of one another if each box in the stack is strictly larger than
# the box above it in width, height, and depth. Implement a method to
# compute the height of the tallest possible stack. The height of a
# stack is the sum of the heights of each box.
import time
NUM_BOXES = 5
boxes = list(range(NUM_BOXES))
w = [4, 7, 5, 8, 4]
h = [2, 5, 3, 8, 2]
d = [6, 7, 3, 5, 2]


def stackable(i, j):
    return i == -1 or (w[i] > w[j] and d[i] > d[j] and h[i] > h[j])


def stackBoxesMaxHeight(leftBoxes, lastBox=-1, lastHeight=0, currentMaxHeight=0):
    global h
    # noNewStackableBox = True
    if leftBoxes:
      for boxIdx in leftBoxes:
          if stackable(lastBox, boxIdx):
              # noNewStackableBox = False
              newLeftBoxes = leftBoxes[:]
              newLeftBoxes.remove(boxIdx)
              newMaxHeight = stackBoxesMaxHeight(newLeftBoxes, boxIdx, lastHeight + h[boxIdx], currentMaxHeight)
              currentMaxHeight = max(newMaxHeight, currentMaxHeight)
              # return max(newMaxHeight, currentMaxHeight)
    # if noNewStackableBox:
    return max(lastHeight, currentMaxHeight)
start = time.process_time()
mh = stackBoxesMaxHeight(boxes)
end = time.process_time()
print((end-start) * 10000000)

######## Solution ########
from operator import attrgetter
class Box:
  def __init__(self, w, h, d):
    self.w = w
    self.h = h
    self.d = d

  def __gt__(self, other):
    return self.w > other.w and self.h > other.h and self.d > other.d

def calcMaxStackHeight(boxes):
  boxes.sort(key=attrgetter('h'), reverse=True)
  maxStackHeight = 0
  memo = {}
  for i in range(len(boxes)):
    height = calcMaxStackHeightWithMemo(i, boxes, memo)
    if height > maxStackHeight:
      maxStackHeight = height
  return maxStackHeight

def calcMaxStackHeightWithMemo(idx, boxes, memo):
  if idx >= len(boxes):
    return 0
  if idx in memo:
    return memo[idx]
  currentHeight = boxes[idx].h
  maxAdditionalHeight = 0
  for i in range(idx+1, len(boxes)):
    if boxes[idx] > boxes[i]:
      additionaHeight = calcMaxStackHeightWithMemo(i, boxes, memo)
      if additionaHeight > maxAdditionalHeight:
        maxAdditionalHeight = additionaHeight
  maxHeight = currentHeight + maxAdditionalHeight
  memo[idx] = maxHeight
  return maxHeight

boxes = []
boxes.append(Box(4,2,6))
boxes.append(Box(7,5,7))
boxes.append(Box(5,3,3))
boxes.append(Box(8,8,5))
boxes.append(Box(4,2,2))

start = time.process_time()
calcMaxStackHeight(boxes)
end = time.process_time()
print((end-start)*1000000)
