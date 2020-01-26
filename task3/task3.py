import sys

cash1 = []
cash2 = []
cash3 = []
cash4 = []
cash5 = []

with open(sys.argv[1]+'/Cash1.txt') as inf:
    for line in inf:
        cash1 += [float(line)]

with open(sys.argv[1]+'/Cash2.txt') as inf:
    for line in inf:
        cash2 += [float(line)]

with open(sys.argv[1]+'/Cash3.txt') as inf:
    for line in inf:
        cash3 += [float(line)]

with open(sys.argv[1]+'/Cash4.txt') as inf:
    for line in inf:
        cash4 += [float(line)]

with open(sys.argv[1]+'/Cash5.txt') as inf:
    for line in inf:
        cash5 += [float(line)]

sum_cash = []
for i in range(0, 16):
    sum_cash += [cash1[i] + cash2[i] + cash3[i] + cash4[i] + cash5[i]]

print(sum_cash.index(max(sum_cash)) + 1)
