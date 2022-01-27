"""

(복습) 백준 문제 2252번 줄 세우기

위상정렬 문제인것을 문제만 읽고 캐치하는 능력이 필요하다.

"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indicies = [0] * (n + 1)
result = []
for _ in range(m):
    a, b = map(int, input().split())
    indicies[b] += 1
    graph[a].append(b)

q = deque()
for i in range(1, n + 1):
    if indicies[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    print(node, end = ' ')
    indicies[node] = -1
    for next_node in graph[node]:
        indicies[next_node] -= 1
        if indicies[next_node] == 0:
            q.append(next_node)