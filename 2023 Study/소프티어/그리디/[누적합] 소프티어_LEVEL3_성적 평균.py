import sys

input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))
for i in range(n - 1):
    scores[i + 1] += scores[i]

for _ in range(k):
    a, b = map(int, input().split())
    a, b = (a - 1), (b - 1)

    exceptValue = scores[a - 1] if (a - 1) >= 0 else 0
    totalValue = scores[b]
    average = round((totalValue - exceptValue) / ((b - a) + 1), 2)

    print(f"{average:.2f}")