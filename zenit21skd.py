import math
import sys

dni = input()
pripady = []
max = -999999999
lepsie = 0
horsie = 0
najvacsie = 0

for i in dni:
    pripady.append(input())

predvcerom = -1

for i in range(1, int(dni)):
    if pripady[i]>pripady[i-1]:
        horsie += 1

    if pripady[i]<pripady[i-1]:
        lepsie += 1

    if predvcerom<int(pripady[i-1]) and pripady[i]<pripady[i-1] and predvcerom!=-1:
        najvacsie += 1

    predvcerom = pripady[i-1]

print(lepsie, " ", horsie, " ", najvacsie)



