"""

백준 문제 1261번 그래프 탐색_알고스팟

DFS/BFS 문제이다.
BFS를 사용해서 푸는것이 문제설계상 편리하고 좋다.
기존에 비슷하던 문제중에서 살짝 한 부분을 꼬와버린 문제이다.

이 문제의 포인트는 distance라는 2차원 배열을 두는것이고, deque를 사용하는것이다,
또 graph[nx][ny] == 0 일때는 appendleft로 순서를 당겨서 처리 해주는것이다.

복습하자

"""

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
graph = []
for i in range(n):
    graph.append(list(map(int, list(input().rstrip()))))
distance = [[-1] * m for _ in range(n)]
distance[0][0] = 0

q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if 0 <= nx < n and 0 <= ny < m:
            if distance[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    q.appendleft((nx, ny)) # 이게 제일 중요
                    distance[nx][ny] = distance[x][y]
                else:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1

print(distance[n - 1][m - 1])