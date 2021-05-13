"""

deque를 사용하지 않고 풀었을때는 쓸데없는 반복문이 많아져서 효율성이 떨어졌었고,
while cities 조건을 거는바람에 잘 풀수가 있었다.

"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
roads = deque(map(int, input().split()))
cities = deque((map(int, input().split())))
base_city = cities.popleft()
answer, cost = 0, roads.popleft()

while cities:
    next_city = cities.popleft()
    if roads:
        if base_city < next_city:
            cost += roads.popleft()
        else:
            answer += (base_city * cost)
            base_city = next_city
            cost = roads.popleft()
print(answer + (base_city * cost))