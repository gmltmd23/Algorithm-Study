import sys
from heapq import *

input = sys.stdin.readline

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
D = [[10 ** 18 for _ in range(10)] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

ans = -1
PQ = []
D[1][0] = 0
heappush(PQ, (D[1][0], 1, 0))
while PQ:
    cd, cur, prev = heappop(PQ)
    if cd > D[cur][prev]:
        continue
    if cur == N:
        ans = cd
        break
    for next, nd in G[cur]:
        if cd + nd >= D[next][cur % A[next]]:
            continue
        if cur != 1 and prev % A[cur] != next % A[cur]:
            continue
        D[next][cur % A[next]] = cd + nd
        heappush(PQ, (cd + nd, next, cur % A[next]))

print(ans)