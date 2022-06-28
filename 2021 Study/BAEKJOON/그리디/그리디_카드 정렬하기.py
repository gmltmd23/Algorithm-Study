"""

문제를 좀 잘못이해해서, 계속 오류가 났던문제
카드뭉치가 1개일때는 비교자체를 안해도되서 결과값이 0이되면 되는데
카드뭉치의 integer값을 리턴해줘서 틀렸었던 문제

고쳐주니깐 바로맞았다.

"""

import sys
import heapq
input = sys.stdin.readline

n, q = int(input().rstrip()), []
for i in range(n):
    q.append(int(input().rstrip()))
heapq.heapify(q)
result = 0

while len(q) > 1:
    first, second = heapq.heappop(q), heapq.heappop(q)
    heapq.heappush(q, first + second)
    result += (first + second)

print(result)