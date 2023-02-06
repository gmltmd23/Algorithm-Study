from math import sqrt
import sys

input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m, q = map(int, input().split())
answer = []

def takeSeat(number, seatSet, eatingMap):
    if len(seatSet) == (n * m):
        x, y = (1, 1)
        seatSet.remove((x, y))
        eatingMap[number] = (x, y)
        for i in range(1, 4, 2):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 < nx <= n and 0 < ny <= m and (nx, ny) in seatSet:
                seatSet.remove((nx, ny))
        answer.append(f"{number} gets the seat ({x}, {y}).")
        return

    safetyPointMap = dict()
    for x, y in seatSet:
        if (x, y) not in safetyPointMap:
            safetyPointMap[(x, y)] = int(1e9)
        for eatingPersonId in eatingMap:
            eatingX, eatingY = eatingMap[eatingPersonId]
            safetyPointMap[(x, y)] = min(safetyPointMap[(x, y)], pow((x - eatingX), 2) + pow((y - eatingY), 2))

    safetyPointList = []
    for key in safetyPointMap:
        x, y = key
        safetyPoint = safetyPointMap[key]
        safetyPointList.append([x, y, safetyPoint])
    safetyPointList.sort(key=lambda x: (-x[2], x[0], x[1]))

    if safetyPointList:
        x, y = safetyPointList[0][0], safetyPointList[0][1]
        seatSet.remove((x, y))
        eatingMap[number] = (x, y)
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 < nx <= n and 0 < ny <= m and (nx, ny) in seatSet:
                seatSet.remove((nx, ny))
        answer.append(f"{number} gets the seat ({x}, {y}).")
        return

    answer.append("There are no more seats.")

def leaveSeat(number, seatSet, doneSet, eatingMap):
    x, y = eatingMap[number]
    doneSet.add(number)
    del eatingMap[number]
    seatSet.add((x, y))
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if 0 < nx <= n and 0 < ny <= m:
            seatSet.add((nx, ny))
    answer.append(f"{number} leaves from the seat ({x}, {y}).")

eatingMap = dict()
doneSet, seatSet = set(), set()
for x in range(1, n + 1):
    for y in range(1, m + 1):
        seatSet.add((x, y))

for _ in range(q):
    command, number = input().split()
    if command == 'In':
        if number in eatingMap:
            answer.append(f"{number} already seated.")
        elif number in doneSet:
            answer.append(f"{number} already ate lunch.")
        else:
            takeSeat(number, seatSet, eatingMap)
    else:
        if number not in doneSet and number not in eatingMap:
            answer.append(f"{number} didn't eat lunch.")
        elif number in doneSet:
            answer.append(f"{number} already left seat.")
        elif number in eatingMap:
            leaveSeat(number, seatSet, doneSet, eatingMap)

print("\n".join(answer))