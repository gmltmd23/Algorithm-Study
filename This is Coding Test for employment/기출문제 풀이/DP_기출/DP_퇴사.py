import sys
import copy
input = sys.stdin.readline

n = int(input().rstrip())
time, pay = [], []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

max_pay = -1
for i in range(n):
    now, next = i, i + time[i]
    temp = copy.deepcopy(pay)
    while next < n:
        temp[next] += temp[now]
        next_time = next + time[next]
        if next_time >= n:
            next = next_time
            continue
        max_pay = max(max_pay, temp[next])
        now = next
        next = next_time

print(max_pay)