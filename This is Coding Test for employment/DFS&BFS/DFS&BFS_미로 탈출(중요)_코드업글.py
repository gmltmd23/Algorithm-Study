from collections import deque

def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 >= nx or nx >= n or -1 >= ny or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))

    return graph[-1][-1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # LRUD

print(bfs(0, 0))