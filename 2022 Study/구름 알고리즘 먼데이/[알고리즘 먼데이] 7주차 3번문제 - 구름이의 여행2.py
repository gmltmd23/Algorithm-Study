import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n, m, k = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited[k] = True
q = deque()
q.append([k, 1])

answer = INF

while q:
    node, count = q.popleft()
    for nextNode in graph[node]:
        if not visited[nextNode]:
            visited[nextNode] = True
            q.append([nextNode, count + 1])
        if nextNode == k:
            answer = min(answer, count)
            break

print(answer if answer != INF else -1)