from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

def dfs(graph, zeroPosList, x, y):
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1 or graph[nx][ny] == 2:
            continue
        graph[nx][ny] = 1
        zeroPosList.append([nx, ny])
        dfs(graph, zeroPosList, nx, ny)

def goVirus(graph, x, y):
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] != 0:
            continue
        graph[nx][ny] = 2
        goVirus(graph, nx, ny)

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m = map(int, input().split())
graph = []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

zeroPosList, virusPosList = [], []
findZeroPosGraph = deepcopy(graph)
for x in range(n):
    for y in range(m):
        if findZeroPosGraph[x][y] == 0:
            findZeroPosGraph[x][y] = 1
            zeroPosList.append([x, y])
            dfs(findZeroPosGraph, zeroPosList, x, y)
        if graph[x][y] == 2:
            virusPosList.append([x, y])

result = 0
wallPosList = list(combinations(zeroPosList, 3))
for wallPos in wallPosList:
    tempGraph = deepcopy(graph)
    first, second, third = wallPos
    tempGraph[first[0]][first[1]], tempGraph[second[0]][second[1]], tempGraph[third[0]][third[1]] = 1, 1, 1

    for virusPos in virusPosList:
        vX, vY = virusPos
        goVirus(tempGraph, vX, vY)

    tempResult = 0
    for i in range(n):
        for j in range(m):
            if tempGraph[i][j] == 0:
                tempResult += 1
    result = max(result, tempResult)

print(result)