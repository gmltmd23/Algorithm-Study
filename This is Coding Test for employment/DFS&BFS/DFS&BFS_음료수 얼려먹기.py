import copy

def dfs(graph, node, visited, check):
    x, y = node
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # LRUD
    if visited[x][y] == 0:
        visited[x][y] = 1
        check.append(1)

    for dir in range(4):
        nx, ny = (x + dx[dir]), (y + dy[dir])
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if visited[nx][ny] == 0:
                dfs(graph, (nx, ny), visited, check)

    return check


n, m = map(int, input().split())
count = 0
ice_frame = []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # LRUD
for i in range(n):
    ice_frame.append(list(map(int, input())))
visited = copy.deepcopy(ice_frame)

answer = []
for i in range(n):
    for j in range(m):
        temp = dfs(ice_frame, (i, j), visited, [])
        if len(temp) >= 1:
            answer.append(temp)

print(len(answer))
