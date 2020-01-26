import sys
import math
import statistics 

def percentile(x):
    x = sorted(x)
    n = (0.9* (len(x) - 1) + 1)
    n1 = x[math.floor(n) - 1]
    n2 = x[math.floor(n)]
    dn = n % 1
    return n1 + dn*(n2 - n1)

l = []
with open(sys.argv[1]) as inf:
    for line in inf:
        l += [int(line.strip())]

print("{0:.2f}".format(percentile(l)))
print("{0:.2f}".format(statistics.median(l)))
print("{0:.2f}".format(max(l)))
print("{0:.2f}".format(min(l)))
print("{0:.2f}".format(statistics.mean(l)))