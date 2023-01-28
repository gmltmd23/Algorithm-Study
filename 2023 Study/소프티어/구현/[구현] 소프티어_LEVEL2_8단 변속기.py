import sys
input = sys.stdin.readline

w, n = map(int, input().split())
jewels = []
for _ in range(n):
    m, p =  map(int, input().split())
    jewels.append((m, p))
jewels.sort(key = lambda x: x[1], reverse = True)

total_weight, answer = 0, 0
for m, p in jewels:
    if (total_weight + m) < w:
        total_weight += m
        answer += (m * p)
    else:
        leftover = (w - total_weight)
        answer += (leftover * p)
        break

print(answer)