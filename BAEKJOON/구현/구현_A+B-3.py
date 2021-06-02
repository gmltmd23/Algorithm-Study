"""

문제 10950 A + B - 3

구현문제이긴한데, 너무 쉬웠습니다..

"""

import sys
input = sys.stdin.readline

T = int(input().rstrip())
for t in range(T):
    print(sum(map(int, input().split())))