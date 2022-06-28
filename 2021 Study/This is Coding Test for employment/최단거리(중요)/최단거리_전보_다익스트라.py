import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(sender):
    q = []
    heapq.heappush(q, (0, sender))
    distance[sender] = 0
    while q:
        time, node = heapq.heappop(q)
        if time > distance[node]:
            continue
        for i in graph[node]:
            cost = time + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m, sender = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra(sender)

count = 0
max_time = 0
for i in range(1, n + 1):
    if distance[i] != 0 and distance[i] != INF:
        count += 1
        max_time = max(max_time, distance[i])

print(count, max_time)