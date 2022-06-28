"""

백준 문제 11650번 좌표 정렬하기

아주 단순한 정렬문제이다.
시간될때 C++로도 풀어봐야겠다.

"""

import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append([a, b])
data.sort()

for a, b in data:
    print(a, b)