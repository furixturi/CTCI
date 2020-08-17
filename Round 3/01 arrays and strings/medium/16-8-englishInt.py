# English Int: Given any integer, print an English phrase that describes
# the integer (e.g., "One Thou­sand, Two Hundred Thirty Four").
import math
ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
  'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
  'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
  'Eighty', 'Ninety']
bigs = ['', '', 'Thousand', 'Million', 'Trillion', 'Quadrillion']

def convert(n, idx=0, res=None):
  if n == 0:
    return ones[0]
  if n < 0:
    return 'Negative ' + convert(-1 * n)
  if idx == 0 and res is None:
    res = []
  s = str(n)
  numOfChunks = math.ceil((len(s)-idx)/3)
  nextIdx = idx+3 if (len(s)-idx) % 3 == 0 else (len(s)-idx) % 3
  chunkRes = convertChunk(s[idx:nextIdx])
  if chunkRes != '':
    chunkRes += ' ' + bigs[numOfChunks]
    res.append(chunkRes)
  if nextIdx < len(s):
    return convert(n, nextIdx, res)
  return ', '.join(res)

def convertChunk(s):
  n = int(s)
  res = []
  if n > 99:
    res.append(ones[n//100] + ' ' + 'Hundred')
  smallPart = n % 100
  if smallPart > 0:
    if smallPart > 19:
      tenDigit = smallPart // 10
      res.append(tens[tenDigit])
      oneDigit = smallPart % 10
      if oneDigit > 0:
        res.append(ones[oneDigit])
    else:
      res.append(ones[smallPart])
  return ' '.join(res)

if __name__ == '__main__':
  # print(convertChunk('12'))
  # print(convertChunk('123'))
  # print(convertChunk('100'))
  # print(convertChunk('119'))

  # print(convert(0))
  # print(convert(10))
  # print(convert(15))
  # print(convert(25))
  # print(convert(100))
  # print(convert(118))
  # print(convert(126))

  print(convert(1024))
  print(convert(1000))
  print(convert(1019))
  print(convert(10000))
  print(convert(100000))
  print(convert(1000000))
  print(convert(100024))
  print(convert(1000024))
  print(convert(10000024))
  print(convert(1000224))
  print(convert(10002424))
  print(convert(123456789))
  print(convert(-123456789))
