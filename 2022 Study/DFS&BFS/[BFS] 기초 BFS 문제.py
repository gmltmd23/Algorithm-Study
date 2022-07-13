from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m = map(int, input().split())

def bfs(graph, x, y):
    q = deque()
    q.append([x, y])

    while q:
        currentX, currentY = q.popleft()
        for i in range(4):
            nx, ny = (currentX + dx[i]), (currentY + dy[i])
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if nx == 0 and ny == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[currentX][currentY]
                q.append([nx, ny])

    return graph[n - 1][m - 1]


graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

print(bfs(graph, 0, 0))