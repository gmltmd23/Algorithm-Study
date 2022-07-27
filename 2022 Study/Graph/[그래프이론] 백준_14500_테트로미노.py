import sys
input = sys.stdin.readline

def dfs(x, y, nowSum, count):
    global maxValue
    if count == 4:
        maxValue = max(maxValue, nowSum)
        return

    for i in range(4):
        nx, ny = (x + moveDirection[i][0]), (y + moveDirection[i][1])
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, nowSum + graph[nx][ny], count + 1)
            visited[nx][ny] = False

def mountainTetromino(x, y):
    global maxValue
    fourMountain = [
        [(x - 1, y), (x, y - 1), (x, y + 1)],
        [(x + 1, y), (x, y - 1), (x, y + 1)],
        [(x, y + 1), (x - 1, y), (x + 1, y)],
        [(x, y - 1), (x - 1, y), (x + 1, y)]
    ]

    for i in range(4):
        nowSum = graph[x][y]
        isIncludeGraph = True
        eachMountain = fourMountain[i]
        for nx, ny in eachMountain:
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                isIncludeGraph = False
                break
            nowSum += graph[nx][ny]
        if isIncludeGraph:
            maxValue = max(maxValue, nowSum)


moveDirection = [(0, -1), (0, 1), (-1, 0), (1, 0)] # LRUD
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
maxValue = 0

for x in range(n):
    for y in range(m):
        visited[x][y] = True
        dfs(x, y, graph[x][y], 1)
        visited[x][y] = False
        mountainTetromino(x, y)

print(maxValue)