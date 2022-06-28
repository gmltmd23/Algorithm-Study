"""

문제가 잘 이해가 되지는 않았다.
여러번 봐야되는 문제이다.

"""

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
sequence = []
for i in range(n):
    sequence.append(int(input().rstrip()))
sequence.sort()

start, end = sequence[1] - sequence[0], sequence[-1] - sequence[0] # 최소갭, 최대갭 구하기

while start <= end:
    center = (start + end) // 2
    value = sequence[0]
    count = 1
    for i in range(1, n):
        if sequence[i] >= value + center:
            value = sequence[i]
            count += 1
    if count >= c:
        start = center + 1
        result = center
    else:
        end = center - 1

print(result)