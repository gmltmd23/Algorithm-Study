"""

문제 10815 숫자 카드

이진탐색 문제중 기본중 기본이다.
쉽게 풀수있음

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
cards = sorted(list(map(int, input().split())))
m = int(input().rstrip())
targets = list(map(int, input().split()))
result = []

for target in targets:
    start, end, hasNumber = 0, n - 1, 0
    while start <= end:
        mid = (start + end) // 2
        if target > cards[mid]:
            start = mid + 1
        elif target < cards[mid]:
            end = mid - 1
        else:
            hasNumber = 1
            break
    result.append(hasNumber)

for res in result:
    print(res, end = ' ')