# Coins: Given an infinite number of quarters (25 cents), dimes (10
# cents), nickels (5 cents), and pennies (1 cent), write code to
# calculate the number of ways of representing n cents.
import time

def makeChanges(sum):
  coins=[5, 25,10,1]
  result = []
  makeChangeWithCoins(sum, coins, {}, result)
  return result

def makeChangeWithCoins(remaining, coins, lastSelection, results):
  coins = [coin for coin in coins if coin <= remaining]
  if len(coins) == 0:
    if remaining == 0:
      # oneResult = {key:value for (key, value) in lastSelection.items() if value > 0}
      results.append(lastSelection)
    return
  coin = coins.pop()
  maxCoin = remaining // coin
  if len(coins) == 0:
    cacheLastSelection = lastSelection[coin] if coin in lastSelection else 0 
    lastSelection[coin] = maxCoin
    remaining -= coin * maxCoin
    makeChangeWithCoins(remaining, coins, lastSelection, results)
    remaining += coin * maxCoin
    lastSelection[coin] = cacheLastSelection
  else:
    for i in range(maxCoin+1):
      cacheLastSelection = lastSelection[coin] if coin in lastSelection else 0 
      remaining -= coin * i
      lastSelection[coin] = i
      makeChangeWithCoins(remaining, coins, lastSelection, results)
      remaining += coin * i
      lastSelection[coin] = cacheLastSelection

############ Optimization #############
def makeChangesWithMemo(sum, coinIdx=0, memo={}):
  coins = [25, 10, 5, 1]
  if sum < 0 or coinIdx >= len(coins):
    return []
  if sum == 0:
    return [{25: 0, 10: 0, 5: 0, 1: 0}]
  if (coins[coinIdx], sum) in memo:
    return memo[(coins[coinIdx], sum)]
  coin = coins[coinIdx]
  if coinIdx == len(coins) - 1:
    return [{coin: sum}]
  result = []
  for i in range(0, sum // coin + 1):
    remaining = sum - coin * i
    waysOfChangesForRemaining = makeChangesWithMemo(remaining, coinIdx+1, memo)
    for way in waysOfChangesForRemaining:
      wayWithCoin = way.copy()
      wayWithCoin[coin] = i
      result.append(wayWithCoin)
  memo[(coin, sum)] = result
  return result

start = time.process_time()
result = makeChanges(200)
end = time.process_time()
print(len(result))
print((end- start)*1000)

start = time.process_time()
result = makeChangesWithMemo(200)
end = time.process_time()
print(len(result))
print((end-start)*1000)
