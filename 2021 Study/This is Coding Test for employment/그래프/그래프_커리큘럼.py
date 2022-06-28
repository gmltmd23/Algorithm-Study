from collections import deque
import sys
import copy
input = sys.stdin.readline

n = int(input())
times, indegree = ([0] * (n + 1)), ([0] * (n + 1))
edges = [[] for i in range(n + 1)]
q = deque()
for i in range(1, n + 1):
    values = list(map(int, input().split()))
    indegree[i] = len(values) - 2
    times[i] = values[0]
    for j in range(1, indegree[i] + 1):
        edges[values[j]].append(i)

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

result = copy.deepcopy(times)
while q:
    index = q.popleft()
    for i in edges[index]:
        result[i] = max(result[i], result[index] + times[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n + 1):
    print(result[i])