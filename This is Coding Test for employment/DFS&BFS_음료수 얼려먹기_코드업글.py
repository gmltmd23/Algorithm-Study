def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        for dir in range(4):
            dfs(x + dx[dir], y + dy[dir])
        return True
    return False

n, m = map(int, input().split())
graph = []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # L R U D
for i in range(n):
    graph.append(list(map(int, input())))

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1
print(answer)
