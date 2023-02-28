from collections import deque
import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def bfs(graph):
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))

    goodbyeSet = set()
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == ICE:
                    visited[nx][ny] += 1
                    if visited[nx][ny] >= 2:
                        goodbyeSet.add((nx, ny))
                elif graph[nx][ny] == EMPTY and visited[nx][ny] == 0:
                    visited[nx][ny] += 1
                    q.append((nx, ny))

    goodbyeIceCount = len(goodbyeSet)
    while goodbyeSet:
        x, y = goodbyeSet.pop()
        graph[x][y] = EMPTY

    return goodbyeIceCount

EMPTY, ICE = 0, 1
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

n, m = map(int, input().split())
graph, iceCount = [], 0
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(m):
        if graph[x][y] == ICE:
            iceCount += 1

answer = 0
while iceCount > 0:
    iceCount -= bfs(graph)
    answer += 1

print(answer)