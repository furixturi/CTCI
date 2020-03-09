# Paint Fill: Implement the "paint fill" function that one might see on
# many image editing programs. That is, given a screen (represented by a
# two-dimensional array of colors), a point, and a new color, fill in
# the surrounding area until the color changes from the original color.
def paintFill(screen, x, y, newColor, oldColor=None, checked=None):
  if oldColor is None:
    oldColor = screen[y][x]
  if checked is None:
    checked = set()

  if (x, y) in checked or x < 0 or y < 0 or y >= len(screen) or x >= len(screen[0]) or screen[y][x] != oldColor:
    return

  screen[y][x] = newColor
  checked.add((x, y))

  # up
  paintFill(screen, x, y - 1, newColor, oldColor, checked)
  # left
  paintFill(screen, x - 1, y, newColor, oldColor, checked)
  # right
  paintFill(screen, x + 1, y, newColor, oldColor, checked)
  # down
  paintFill(screen, x, y + 1, newColor, oldColor, checked)
