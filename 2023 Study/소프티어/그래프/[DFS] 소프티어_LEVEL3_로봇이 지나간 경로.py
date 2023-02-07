import sys
from copy import deepcopy

input = sys.stdin.readline


def selectDirection(nowDirection, nextDirection):
    left, right = nowDirection, nowDirection

    leftCount = 0
    while left != nextDirection:
        left -= 1
        if left < 0:
            left = 3
        leftCount += 1

    rightCount = 0
    while right != nextDirection:
        right = (right + 1) % 4
        rightCount += 1

    if leftCount <= rightCount:
        return 'L' * leftCount
    else:
        return 'R' * rightCount


def dfs(x, y, direction, commandList, nowSharpCount):
    global answerCommandList, answerX, answerY, answerDirection
    if nowSharpCount == sharpCount:
        answerCommandList[-1].append(deepcopy(commandList))
        return

    for i in range(4):
        ax, ay = (x + dx[i]), (y + dy[i])
        bx, by = (x + dx[i] + dx[i]), (y + dy[i] + dy[i])
        if 0 <= ax < h and 0 <= bx < h and 0 <= ay < w and 0 <= by < w:
            if graph[ax][ay] and graph[bx][by]:
                graph[ax][ay], graph[bx][by] = False, False
                directionString = selectDirection(direction, i)
                for j in range(len(directionString)):
                    commandList.append(directionString[j])
                commandList.append('A')
                dfs(bx, by, i, commandList, nowSharpCount + 2)
                commandList.pop()
                for j in range(len(directionString)):
                    commandList.pop()
                graph[ax][ay], graph[bx][by] = True, True


directionList = ['<', '^', '>', 'v']  # LURD
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]  # LURD
h, w = map(int, input().split())
graph = []
answerCommandList = []
sharpCount = 0
for i in range(h):
    graph.append([])
    line = list(input().rstrip())
    for j in range(w):
        if line[j] == '#':
            sharpCount += 1
            graph[-1].append(True)
        else:
            graph[-1].append(False)

for x in range(h):
    for y in range(w):
        if graph[x][y]:
            for i in range(4):
                ax, ay = (x + dx[i]), (y + dy[i])
                bx, by = (x + dx[i] + dx[i]), (y + dy[i] + dy[i])
                if 0 <= ax < h and 0 <= bx < h and 0 <= ay < w and 0 <= by < w:
                    if graph[ax][ay] and graph[bx][by]:
                        graph[x][y], graph[ax][ay], graph[bx][by] = False, False, False
                        answerCommandList.append([x + 1, y + 1, i])
                        dfs(bx, by, i, ['A'], 3)
                        graph[x][y], graph[ax][ay], graph[bx][by] = True, True, True
                        if len(answerCommandList[-1]) <= 3:
                            answerCommandList.pop()

answerCommandList.sort(key = lambda x : (len(x[3])))
print(answerCommandList[0][0], answerCommandList[0][1])
print(directionList[answerCommandList[0][2]])
print("".join(answerCommandList[0][3]))