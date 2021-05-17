"""

문제 2178 미로 탐색

처음에는 재귀로 풀었더니, 메모리 초과나서
deque를 사용해서, 반복문 방식으로 바꾸니깐 잘풀렸다.

"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(pos):
    q = deque()
    q.append(pos)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] != 1 or (nx == 0 and ny == 0):
                continue
            q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

    print(graph[n - 1][m - 1])

n, m = map(int, input().split())
graph = []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
bfs((0, 0))