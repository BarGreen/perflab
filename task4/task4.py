import sys

# Обработка входных данных:
time_bank = []
with open(sys.argv[1]) as inf:
    for line in inf:
        i = line.strip().split()
        for j in i:
            time_bank += [int(k) for k in j.split(":")]

timestamp_bank = []
i = 0
while i < len(time_bank):
    timestamp_bank += [time_bank[i]*60 + time_bank[i + 1]]
    i += 2

# Массив времени:
time_matrix = []
for i in range (480, 1201):
    time_matrix += [[i, 0]]

# Счетчик:
j = 0
k = timestamp_bank[j]
while j <= len(timestamp_bank) - 2:
    for n in time_matrix:
        if k == n[0]:
            n[1] += 1
    if k != timestamp_bank[j + 1] - 1:
        k += 1
    else:
        if j == len(timestamp_bank) - 2 and k == timestamp_bank[j + 1] - 1:
            break
        j += 2
        k = timestamp_bank[j]

# Массив выходных данных:
final = []
i = []
for f in range(0, len(time_matrix)):
    i += [time_matrix[f][1]]

for f in range(0, len(time_matrix)):
    if time_matrix[f][1] == max(i):
        final += [time_matrix[f][0]]

Y = [final[0]]
for f in range(len(final) - 1):
    if final[f] != final[f + 1] - 1:
        Y += [final[f] + 1]
        Y += [final[f + 1]]
Y += [final[-1] + 1]

# Обработка выходных данных:
output = []
out = 0
while out < len(Y):
    output += [[str(Y[out] // 60) + ":" + str(Y[out] % 60), str(Y[out + 1] // 60) 
    + ":" + str(Y[out + 1] % 60)]]
    out += 2

for j in output:
    if j[0][-2] == ":" and j[1][-2] == ":":
            print(j[0] + "0", ' ', j[1] + "0")
    elif j[0][-2] == ":":
            print(j[0] + "0", ' ', j[1])
    elif j[1][-2] == ":":
            print(j[0], ' ', j[1] + "0")
    else:
        print(j[0], ' ', j[1])