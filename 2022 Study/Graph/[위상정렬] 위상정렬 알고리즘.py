from collections import deque
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

answer = []
while q:
    node = q.popleft()
    answer.append(node)
    for target in graph[node]:
        indegree[target] -= 1
        if indegree[target] == 0:
            q.append(target)

print(answer)