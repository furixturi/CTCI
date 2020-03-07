# Triple Step: A child is running up a staircase with n steps and can
# hop either 1 step, 2 steps, or 3 steps at a time. Implement a method
# to count how many possible ways the child can run up the stairs.
# Hints: #152, #178, #217, #237, #262, #359

# recursive
def ways(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2
  return ways(n-3) + ways(n-2) + ways(n-1)

# recursive with memo
def waysMemo(n, memo = None):
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2
  if memo is None:
    memo = [None] * (n + 1)
  if memo[n] is None:
    memo[n] = waysMemo(n-3, memo) + waysMemo(n-2, memo) + waysMemo(n-1, memo)
  return memo[n]

# iterative
def waysIterative(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2
  a = 1
  b = 1
  c = 2
  i = 3
  while i < n:
    c1 = a + b + c
    b = c
    a = b
    c = c1
    i += 1
  return a + b + c