"""

시간초과나서 pypy3로 제출하니깐 잘 풀렸다.

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
while start <= end:
    left_over = 0
    center = (start + end) // 2
    for t in trees:
        if t > center:
            left_over += (t - center)
    if left_over >= m:
        start = center + 1
    else:
        end = center - 1
print(end)