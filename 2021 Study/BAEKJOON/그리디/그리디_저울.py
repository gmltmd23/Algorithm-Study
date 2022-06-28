"""

문제 2437 저울

그리디 문제인데, 단순한 아이디어를 떠올리기 어려운 문제이다.

한번 복습해보면 좋을거같다.

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
weight = sorted(list(map(int, input().split())))

target = 1
for element in weight:
    if target < element:
        break
    target += element
print(target)