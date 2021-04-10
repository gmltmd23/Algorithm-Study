import sys
input = sys.stdin.readline
INF = int(1e9)

def get_smallest_node():
    min_value, index = INF, 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start_node):
    visited[start_node], distance[start_node] = True, 0
    for i in graph[start_node]:
        distance[i[0]] = i[1]

    for i in range(n - 1):
        node = get_smallest_node()
        visited[node] = True
        for j in graph[node]:
            cost = distance[node] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited, distance = [False] * (n + 1), [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])