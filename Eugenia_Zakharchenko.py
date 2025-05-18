from const import *
ones = 0
summ = 0
summ1 = 0

with open(FILE_NAME, 'r') as file:
    lines = file.readlines()
    alchemist = lines[14-1].split(' ')[8-1]
    for i in range(1-1, 24, 1):
        s = lines[i]
        for symbol in s:
            if symbol != ' ' and symbol != '\n':
                summ1 += int(symbol)
    for line in lines:
        for symbol in line:
            if symbol == '1':
                ones += 1
            if symbol != ' ' and symbol != '\n':
                summ += int(symbol)
print(ones)
print(summ)
print(alchemist)
print(summ1)

