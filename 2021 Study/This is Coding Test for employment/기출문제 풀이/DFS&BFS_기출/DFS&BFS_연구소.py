import sys
from collections import deque
import copy
input = sys.stdin.readline

def bfs(pos, temp_map):
    q = deque()
    q.append(pos)
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = (x + dx[dir]), (y + dy[dir])
            if 0 <= nx < n and 0 <= ny < m:
                if temp_map[nx][ny] == 0:
                    temp_map[nx][ny] = 2
                    q.append((nx, ny))

def get_count(temp_map):
    count = 0
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                count += 1
    return count

n, m = map(int, input().split())
graph, cases = [], []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # LRUD
for i in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        cases.append((i, j))

result = 0
for first in cases:
    for second in cases:
        for third in cases:
            if first != second and first != third and second != third:
                temp = copy.deepcopy(graph)
                if temp[first[0]][first[1]] + temp[second[0]][second[1]] + temp[third[0]][third[1]] == 0:
                    temp[first[0]][first[1]] = 1
                    temp[second[0]][second[1]] = 1
                    temp[third[0]][third[1]] = 1
                    for i in range(n):
                        for j in range(m):
                            if temp[i][j] == 2:
                                bfs((i, j), temp)
                    result = max(result, get_count(temp))

print(result)