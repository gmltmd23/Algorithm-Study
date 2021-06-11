"""

복습을 위해 다익스트라 문제를 풀어봤다.

이거는 공식처럼 안까먹기위해 주기적으로 풀어줘야할거같다.

"""


import heapq
import sys
input = sys.stdin.readline
INF = 1e9

def dijkstra(start_node):
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

v, e = map(int, input().split())
start = int(input().rstrip())
distance = [INF] * (v + 1)
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

for i in range(1, v + 1):
    print(distance[i] if distance[i] != INF else 'INF')