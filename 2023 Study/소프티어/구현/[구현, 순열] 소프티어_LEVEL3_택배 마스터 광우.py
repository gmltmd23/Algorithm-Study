import sys
from itertools import permutations
input = sys.stdin.readline

n, m, k = map(int, input().split())
railList = list(map(int, input().split()))

answer = int(1e9)
for eachRailList in list(permutations(railList, n)):
    total, railIndex, workCount = 0, 0, 0
    while workCount < k:
        basket = 0
        while (basket + eachRailList[railIndex]) <= m:
            basket += eachRailList[railIndex]
            railIndex = (railIndex + 1) % n
        total += basket
        workCount += 1
    answer = min(answer, total)

print(answer)