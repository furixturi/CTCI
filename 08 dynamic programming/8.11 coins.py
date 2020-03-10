# Coins: Given an infinite number of quarters (25 cents), dimes (10
# cents), nickels (5 cents), and pennies (1 cent), write code to
# calculate the number of ways of representing n cents.
def makeChanges(sum):
  coins=[5, 25,10,1]
  result = []
  makeChangeWithCoins(sum, coins, {}, result)
  return result

def makeChangeWithCoins(remaining, coins, lastSelection, results):
  coins = [coin for coin in coins if coin <= remaining]
  if len(coins) == 0:
    if remaining == 0:
      oneResult = {key:value for (key, value) in lastSelection.items() if value > 0}
      results.append(oneResult)
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
result = makeChanges(50)
print(result, len(result))