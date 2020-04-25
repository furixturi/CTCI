def fib(i, memo=None):
  if not memo:
    memo = [0, 1] + [None] * (i - 1)
  if memo[i] is not None:
    return memo[i]
  memo[i] = fib(i-2, memo) + fib(i-1, memo)
  return memo[i]

fib8 = fib(8)
print(fib8)