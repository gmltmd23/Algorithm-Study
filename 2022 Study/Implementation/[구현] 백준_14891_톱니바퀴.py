from math import ceil
import sys
input = sys.stdin.readline

n = input().rstrip()
roomNumber = [0] * 10
for i in n:
    roomNumber[int(i)] += 1

maxNumber = 0
sixAndNine = 0
for number in range(len(roomNumber)):
    if number != 6 and number != 9:
        maxNumber = max(maxNumber, roomNumber[number])
    else:
        sixAndNine += roomNumber[number]
maxNumber = max(maxNumber, ceil(sixAndNine / 2))

print(maxNumber)