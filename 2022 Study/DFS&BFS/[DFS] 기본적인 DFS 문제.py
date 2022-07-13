import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m = map(int, input().split())

def dfs(graph, x, y):
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if nx < 0 or  nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            dfs(graph, nx, ny)


graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

result = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(graph, x, y)
            result += 1

print(result)