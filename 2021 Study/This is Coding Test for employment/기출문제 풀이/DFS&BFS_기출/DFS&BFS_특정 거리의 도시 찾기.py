import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m, k, x):
    answer = []
    costs = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    q = deque()
    q.append(x)

    while q:
        node = q.popleft()
        for dest in graph[node]:
            if costs[dest] == 0:
                q.append(dest)
                costs[dest] = costs[node] + 1
    
    for node, cost in enumerate(costs):
        if k == cost:
            answer.append(node)
    if len(answer) == 0:
        answer.append(-1)
    
    return answer
            

n, m, k, x = map(int, input().split())
result = bfs(n, m, k, x)
for node in result:
        print(node)