"""

문제 7576 토마토

알고리즘은 잘 짰지만, 시간 초과가 나서, q를 전역변수로 바꿔주니깐 해결됬음

"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 or graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0 or graph[nx][ny] > graph[x][y] + 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

def get_result(graph):
    result = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                return -1
            result = max(result, graph[x][y])
    return result - 1

m, n = map(int, input().split())
q = deque()
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # LRUD
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            q.append((x, y))
bfs()

print(get_result(graph))