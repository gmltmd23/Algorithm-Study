import copy

def bfs(x, y):
    visited[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            temp = graph[x][y] + 1
            if visited[nx][ny] != 0:
                graph[nx][ny] = temp
                bfs(nx, ny)
            else:
                if graph[nx][ny] > temp:
                    graph[nx][ny] = temp


n, m = map(int, input().split())
graph = []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # LRUD
for i in range(n):
    graph.append(list(map(int, input())))
visited = copy.deepcopy(graph)

bfs(0, 0)
for j in graph:
    print(j)