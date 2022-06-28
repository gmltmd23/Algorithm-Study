"""

백준 문제 2109번 그리디_순회강연

정답률 35.932%의 문제였다.
이 문제또한 푸는 방법이 여러가지 있지만, 여러가지 방법들중에
가장 효율성이 좋은 방법은 우선순위 큐를 사용하여 푸는것이다.

복습이 필요한 좋은 문제였다.

"""

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x: x[1])

answer = []
for element in data:
    heappush(answer, element[0])
    if element[1] < len(answer):
        heappop(answer)

print(sum(answer))