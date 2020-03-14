# Boolean Evaluation: Given a boolean expression consisting of the
# symbols 0 (false), 1 (true), & (AND), | (OR), and ^ (XOR), and a
# desired boolean result value result, implement a function to count the
# number of ways of parenthesizing the expression such that it evaluates
# to result.
# EXAMPLE
# countEval("1^0|0|1", false) -> 2
# countEval("0&0&0&1^1|0", true) -> 10

import time
def countEval(expr, expectedResult):
    if len(expr) == 0:
        return 0
    if len(expr) == 1:
        return 1 if bool(int(expr)) == expectedResult else 0

    ways = 0
    for i in range(len(expr)):
        c = expr[i]
        if c == '^' or c == '&' or c == '|':
            leftPartExpr = expr[0:i]
            rightPartExpr = expr[i+1:]
            waysLeftTrue = countEval(leftPartExpr, True)
            waysLeftFalse = countEval(leftPartExpr, False)
            waysRightTrue = countEval(rightPartExpr, True)
            waysRightFalse = countEval(rightPartExpr, False)

            totalWays = waysLeftFalse * waysRightFalse + waysLeftTrue * waysRightTrue + \
                waysLeftTrue * waysRightFalse + waysLeftFalse * waysRightTrue

            if c == '^':
              totalTrue = waysLeftTrue * waysRightFalse + waysLeftFalse * waysRightTrue
            elif c == '&':
              totalTrue = waysLeftTrue * waysRightTrue
            else:
              totalTrue = waysLeftTrue * waysRightTrue + waysLeftTrue * waysRightFalse + waysLeftFalse * waysRightTrue
            
            totalWaysExpectedResult = totalTrue if expectedResult else totalWays - totalTrue
            ways += totalWaysExpectedResult
    return ways

# print(countEval("1^0|0|1", False))
# print(countEval("0&0&0&1^1|0", True))


def countEvalMemo(expr, expectedResult, memo={}):
    if len(expr) == 0:
        return 0
    if len(expr) == 1:
        return 1 if bool(int(expr)) == expectedResult else 0
    if (expr, expectedResult) in memo:
      return memo[(expr, expectedResult)]

    ways = 0
    for i in range(len(expr)):
        c = expr[i]
        if c == '^' or c == '&' or c == '|':
            leftPartExpr = expr[0:i]
            rightPartExpr = expr[i+1:]
            waysLeftTrue = countEval(leftPartExpr, True)
            waysLeftFalse = countEval(leftPartExpr, False)
            waysRightTrue = countEval(rightPartExpr, True)
            waysRightFalse = countEval(rightPartExpr, False)

            totalWays = waysLeftFalse * waysRightFalse + waysLeftTrue * waysRightTrue + \
                waysLeftTrue * waysRightFalse + waysLeftFalse * waysRightTrue

            if c == '^':
              totalTrue = waysLeftTrue * waysRightFalse + waysLeftFalse * waysRightTrue
            elif c == '&':
              totalTrue = waysLeftTrue * waysRightTrue
            else:
              totalTrue = waysLeftTrue * waysRightTrue + waysLeftTrue * waysRightFalse + waysLeftFalse * waysRightTrue
            
            totalWaysExpectedResult = totalTrue if expectedResult else totalWays - totalTrue
            ways += totalWaysExpectedResult
    memo[(expr, expectedResult)] = ways
    return ways

start = time.process_time()
countEval("0&0&0&1|0&0&0", True)
end = time.process_time()
print((end - start) * 1000)

start = time.process_time()
countEvalMemo("0&0&0&1|0&0&0", True)
end = time.process_time()
print((end - start) * 1000)


