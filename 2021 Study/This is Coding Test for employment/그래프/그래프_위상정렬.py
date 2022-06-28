import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

v, e = map(int, input().split())
indegree = [0] * (v + 1)
edges = [[] for _ in range(v + 1)]
result = []
for i in range(e):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1
q = deque()

for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    result.append(node)
    for index in edges[node]:
        indegree[index] -= 1
        if indegree[index] == 0:
            q.append(index)

for i in range(v):
    print(result[i], end = ' ')