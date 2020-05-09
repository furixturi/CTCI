def sortBigFile(file, sortFunc, CHUNK_SIZE=10000):
  chunkFiles = createSortedChunkFiles(file, sortFunc, CHUNK_SIZE)
  mergeWriteSortedChunkFiles(chunkFiles, sortFunc)

def createSortedChunkFiles(file, sortFunc, CHUNK_SIZE):
  chunkFiles = []
  with open(file, 'r') as fin:
    currChunk = []
    currIdx = 0
    chunkIdx = 0
    for line in fin:
      currChunk.append(line)
      currIdx += 1
      if currIdx == CHUNK_SIZE-1:
        with open(f'chunk-{chunkIdx}', 'w+') as fout:
          fout.writelines(sorted(currChunk, key=sortFunc))
          chunkFiles.append(f'chunk-{chunkIdx}')
          chunkIdx += 1
          currIdx = 0
          currChunk = []
  return chunkFiles

def mergeWriteSortedChunkFiles(files, sortFunc):
  w1 = 'out1'
  w2 = 'out2'
  lastFile = files[0]
  currFout = w1
  for i in range(1, len(files)):
    with open(currFout, 'w+') as fout, open(lastFile, 'r') as fin1, open(files[i], 'r') as fin2:
      line1 = fin1.readline()
      line2 = fin2.readline()
      while True:
        if line1 == '' or line2 == '':
          break
        nextLineOut = min(line1, line2, key=sortFunc)
        if nextLineOut == line1:
          line1 = fin1.readline()
        else:
          line2 = fin2.readline()
        fout.write(nextLineOut + '\n')
      if line1 != '' or line2 != '':
        line = line1 if line1 != '' else line2
        remainingFile = fin1 if line1 != '' else fin2
        while line != '':
          fout.write(line + '\n')
          line = remainingFile.readline()
    lastFile = currFout
    currFout = w2 if lastFile == w1 else w1
      