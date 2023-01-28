from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = int(1e9)
dx, dy = [0, 0, -1, 1], [ -1, 1, 0, 0]

def dijkstra(n, graph, distance):
    distance[0][0] = graph[0][0]
    q = []
    heappush(q, [graph[0][0], 0, 0])

    while q:
        nowCost, x, y = heappop(q)
        if distance[x][y] < nowCost:
            continue
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < n and 0 <= ny < n:
                nextCost = nowCost + graph[nx][ny]
                if nextCost < distance[nx][ny]:
                    distance[nx][ny] = nextCost
                    heappush(q, [distance[nx][ny], nx, ny])

    return distance[n - 1][n - 1]

problemCount = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]
    print("Problem {0}: {1}".format(problemCount, dijkstra(n, graph, distance)))
    problemCount += 1