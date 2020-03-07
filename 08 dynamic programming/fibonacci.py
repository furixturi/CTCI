# 0, 1, 1, 2, 3, 5, 8, 13, ...

# not optimized recursion, O(2^n)
def fib(i):
  if i == 0:
    return 0
  if i == 1:
    return 1
  return fib(i-2) + fib(i-1)

# optimize with memoization, O(n)
def fib2(i):
  memo = [-1] * (i + 1) 
  return fibWithMemo(i, memo)

def fibWithMemo(i, memo):
  if i == 0:
    return 0
  if i == 1:
    return 1

  if memo[i] == -1:
    memo[i] = fibWithMemo(i-2, memo) + fibWithMemo(i-1, memo)

  return memo[i]

# optimized iterative solution
def fib3(i):
  if i == 0:
    return 0
  if i == 1:
    return 1
  a = 0
  b = 1
  n = 2
  while n < i:
    c = a + b
    a = b
    b = c
    n += 1
  return a + b                
