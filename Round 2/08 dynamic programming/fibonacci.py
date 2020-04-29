# Top-down - recursion with memo
# Without memo: all sub problems form a huge binary tree
# Time complexity = 2^0 + 2^1 + 2^2 + ... + 2^n = 2^(N+1)-1 = O(2^N)
# With memo: sub problems form a linked list
# Time complexity = O(N)
def fib(i, memo=None):
  if not memo:
    memo = [0, 1] + [None] * (i - 1)
  if memo[i] is not None:
    return memo[i]
  memo[i] = fib(i-2, memo) + fib(i-1, memo)
  return memo[i]

# Bottom-up - iterative
def fibIterative(n):
  if n == 1 or n == 2: return 1
  memo = [0, 1, 1] + [-1] * (n-2)
  i = 3
  while i <= n:
    memo[i] = memo[i-2] + memo[i-1]
    i += 1
  return (memo, memo[n])

# Bottom-up - further optimization on space
def fibOptimized(n):
  if n == 1 or n == 2: return 1
  a = 1
  b = 1
  i = 3
  while i <= n:
    tmp = a + b
    a = b
    b = tmp
    i += 1
  return b
  

fib7 = fib(7)
fib8 = fib(8)
print(fib7, fib8)
memo9, fib9 = fibIterative(9)
print(memo9, fib9)
print(fibOptimized(9))