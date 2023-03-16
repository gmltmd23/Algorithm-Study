from heapq import heappush, heappop
import sys

input = sys.stdin.readline

# DOWN, RIGHT, UP, LEFT // ABCD
direction = dict()
direction['A'] = 0
direction['B'] = 3
direction['C'] = 2
direction['D'] = 1

n = int(input())
line = [[] for _ in range(4)]
answer = [-1] * n

waitQueue = []
for i in range(n):
    targetSecond, targetDirection = input().split()
    heappush(waitQueue, [int(targetSecond), direction[targetDirection], i])

line = [[] for _ in range(4)]
nowSecond = 0
while waitQueue:
    if waitQueue and waitQueue[0][0] > nowSecond:
        nowSecond = waitQueue[0][0]

    while waitQueue and waitQueue[0][0] <= nowSecond:
        targetSecond, targetDirection, index = heappop(waitQueue)
        targetLine = line[targetDirection]
        targetLine.append([targetSecond, index])

    isPassed = False
    for i in range(4):
        if line[i]:
            if len(line[(i + 1) % 4]) >= 1:
                for nextSecond, nowIndex in line[i]:
                    heappush(waitQueue, [nextSecond + 1, i, nowIndex])
            else:
                answer[line[i][0][1]] = nowSecond
                isPassed = True
                for j in range(1, len(line[i])):
                    nextSecond, nowIndex = line[i][j]
                    heappush(waitQueue, [nextSecond + 1, i, nowIndex])

    if not isPassed:
        break

    for i in range(4):
        if line[i]:
            line[i].clear()

for element in answer:
    print(element)