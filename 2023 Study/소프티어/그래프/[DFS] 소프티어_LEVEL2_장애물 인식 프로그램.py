import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def dfs(n, graph, x, y, answer):
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                answer[-1] += 1
                graph[nx][ny] = 0
                dfs(n, graph, nx, ny, answer)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

answer = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            answer.append(1)
            graph[x][y] = 0
            dfs(n, graph, x, y, answer)

answer.sort()
print(len(answer))
for blockCount in answer:
    print(blockCount)