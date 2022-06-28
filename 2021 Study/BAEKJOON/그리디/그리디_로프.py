"""

문제의 조건중에  '모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.' 이거를
명심해서 읽으면 크게 어려울게 없는 문제이다.
최대 힙을 이용해서 풀면 금방 풀수있는 문제

"""

import sys
import heapq
input = sys.stdin.readline

n = int(input())
ropes, result = [], 0
for i in range(n):
    heapq.heappush(ropes, -int(input().rstrip()))
for i in range(1, n + 1):
    result = max(result, -heapq.heappop(ropes) * i)
print(result)