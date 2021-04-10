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

n, m = map(int, input().split()) # 노드, 간선의 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0 # 자기자신으로 가는 노드의 값은 0으로 초기화

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

floyd_warshall()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print('INFINITY', end = '\t')
        else:
            print(graph[i][j], end = '\t')
    print()