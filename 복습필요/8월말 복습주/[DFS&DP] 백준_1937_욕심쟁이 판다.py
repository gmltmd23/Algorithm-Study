import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > graph[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
n = int(input())
graph = []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

answer = 0
dp = [[0] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        answer = max(answer, dfs(x, y))

print(answer)