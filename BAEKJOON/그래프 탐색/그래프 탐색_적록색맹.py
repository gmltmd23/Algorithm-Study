"""

백준 10026번 적록색약

어떻게는 반복문 여러개 쓰지않고 한 큐에 풀고싶어서 오랫동안 고생좀 해봤는데
풀다보니깐 반복문 한개로는 구조적 문제로 풀수가 없다.

눈물을 머금고 반복문을 3~4개 써서 풀었다.

전형적인 DFS/BFS 문제이다.

"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))

    while q:
        bx, by = q.popleft()
        for i in range(4):
            nx, ny = (bx + dx[i]), (by + dy[i])
            if (0 <= nx < n and 0 <= ny < len(graph[0])) and not visited[nx][ny]:
                if graph[bx][by] == graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

n = int(input())
graph, visited = [], []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # LRUD
regular, irregular = 0, 0
for _ in range(n):
    temp = list(input().rstrip())
    graph.append(temp)
    visited.append([False] * len(temp))

for x in range(n):
    for y in range(len(visited[0])):
        if not visited[x][y]:
            bfs(x, y)
            regular += 1

for i in range(n):
    for j in range(len(visited[0])):
        visited[i][j] = False
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for x in range(n):
    for y in range(len(visited[0])):
        if not visited[x][y]:
            bfs(x, y)
            irregular += 1

print(regular, irregular)
