import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd_warshall():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if i == j or i == k:
                    continue
                cost = graph[j][i] + graph[i][k]
                if cost < graph[j][k]:
                    graph[j][k] = cost

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y], graph[y][x] = 1, 1
x, k = map(int, input().split())

floyd_warshall()
result = (graph[1][k] + graph[k][x]) if (graph[1][k] + graph[k][x]) < INF else -1
print(result)