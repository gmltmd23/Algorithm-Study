import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weights = [0] + list(map(int, input().split()))
best = [True] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    if weights[a] <= weights[b]:
        best[a] = False
    if weights[b] <= weights[a]:
        best[b] = False

answer = 0
for i in range(1, n + 1):
    if best[i]:
        answer += 1

print(answer)