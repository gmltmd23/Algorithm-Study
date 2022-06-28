import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd_warshall(graph):
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                first = graph[a][b]
                second = graph[a][k] + graph[k][b]
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1): # 자기 자신으로 가는것은 0으로 초기화
    graph[i][i] = 0
for i in range(m):
    a, b, cost = map(int, input().split())
    if cost < graph[a][b]:
        graph[a][b] = cost

floyd_warshall(graph)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print('INF', end = '\t')
        else:
            print(graph[i][j], end = '\t')
    print()