import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ttoeks = list(map(int, input().split()))
start, end = 0, max(ttoeks)

while start <= end:
    h = (start + end) // 2
    sum = 0
    for i in range(n):
        if ttoeks[i] > h:
            sum += (ttoeks[i] - h)

    if m < sum:
        start = h + 1
    elif m > sum:
        end = h - 1
    else:
        break

print(h)