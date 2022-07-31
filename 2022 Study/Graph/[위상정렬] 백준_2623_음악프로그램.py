from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegree, pdOrderGraph = [0] * (n + 1), [[] for _ in range(n + 1)]
for _ in range(m):
    nowOrderLine = list(map(int, input().split()))[1:]
    for i in range(len(nowOrderLine) - 1):
        if (i + 1) < len(nowOrderLine):
            indegree[nowOrderLine[i + 1]] += 1
            pdOrderGraph[nowOrderLine[i]].append(nowOrderLine[i + 1])

q = deque()
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

result = []
while q:
    result.append(q.popleft())
    for nextSinger in pdOrderGraph[result[-1]]:
        indegree[nextSinger] -= 1
        if indegree[nextSinger] == 0:
            q.append(nextSinger)

if len(result) != n:
    print(0)
else:
    for singer in result:
        print(singer)