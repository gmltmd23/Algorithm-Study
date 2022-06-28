"""

백준 문제 1655번 자료 구조_가운데를 말해요

상당히 좋은 문제이다.
난이도도 있고, 생각도 많이해야 하는 문제이다.
우선순위큐를 두개를 동시에 사용하면 이런식으로도 풀 수 있다는것을 알게해준 문제이다.
고민해보았지만 접근이 어려워 풀이를 참고하게 된 문제였다.

반드시 복습을하고 내것으로 만들어야 겠다.

"""

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
left_heap, right_heap = [], []
for i in range(n):
    number = int(input())
    if len(left_heap) == len(right_heap):
        heappush(left_heap, -number)
    else:
        heappush(right_heap, number)

    if right_heap and -left_heap[0] > right_heap[0]:
        left_value, right_value = -heappop(left_heap), heappop(right_heap)
        heappush(left_heap, -right_value)
        heappush(right_heap, left_value)
    print(-left_heap[0])