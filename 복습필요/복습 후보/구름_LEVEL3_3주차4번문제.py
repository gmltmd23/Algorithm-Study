import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
graph = defaultdict(list)
for i in range(n):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [0 for _ in range(n + 1)]
circle = list()
finded = -1

def FindCycle(u, tar):
    global finded
    if visited[u] == 1:
        finded = u
        if u not in circle:
            circle.append(u)
        return
    visited[u] = 1

    for i in graph[u]:
        if i == tar:
            continue
        FindCycle(i, u)

        if finded == -2:
            return
        if finded == u:
            finded = -2
            return

        if finded >= 0:
            if u not in circle:
                circle.append(u)
            return

FindCycle(1, 1)
circle.sort()

print(len(circle))
for i in circle:
    print(i, end = ' ')