# Find the top ten IP addresses from a web server log file.
# A sample line from the log file:
# 14716104719,GET,/index.html,10.10.10.1

# Sample output:
# RANK, IP, COUNT
# 1, 127.10.24.1, 18975
# 2, 239.19.5.1, 17497
# ...
# 10, 94.104.1.100, 2945


def rankRequests(log):
  count = {}
  lines = log.split('\n')
  for l in lines:
    ip = l.split(',')[3]
    if ip in count:
      count[ip] += 1
    else:
      count[ip] = 1
  sortedRecords = sorted(
    count.items(), key=lambda record: record[1], reverse=True)
  print('RANK, IP, COUNT')
  for i in range(10):
    record = sortedRecords[i]
    print(f'{i+1}, {record[0]}, {record[1]}')
