import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = int(input()), int(input())
graph = [([INF] * (n + 1)) for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if graph[x][y] == INF:
            print(0, end = ' ')
        else:
            print(graph[x][y], end = ' ')
    print()