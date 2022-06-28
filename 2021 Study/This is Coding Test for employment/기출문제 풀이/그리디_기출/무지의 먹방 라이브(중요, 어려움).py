"""

어려운 문제이다.
일단 k의 범위가 1 <= k <= 10 ** 10^16 이므로 배열의 원소를 일일히 들여다보며
계산하는 방식은 무조건 시간초과 또는 런타임 에러가 난다.

k를 단축하는 방법을 찾아야 된다.
그러므로 특정 규칙을 찾아서 한꺼번에 확확 줄이거나,
많은 양을 줄이는데 효과적인 이진 탐색같은것을 이용한다.

여기 적혀져있는 코드는 일단 구현이 안되서 다른사람의것을 참고한 코드이다.
우선순위 큐 (heapq)를 사용해서, 하는 방식인데

먼저 가장 적은시간이 걸리는 음식을 다 먹을때까지 다른 음식은 여전히 남아있다는 점을 이용한 방법이다.
즉 k값과 동일해질때까지 가장 적은 시간이 걸리는 음식을 먼저 죽이는 방식이다.

가장 적은것을 다 먹으면 그 다음으로 가장 적은것을 먹고 .. 이런방식이다.

"""

import heapq
import sys
input = sys.stdin.readline

def solution(food_times, k):
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    sum_value, previous = 0, 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))