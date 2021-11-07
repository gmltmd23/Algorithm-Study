"""

백준 문제 15903번 그리디_카드 합체 놀이

푸는 방법이 2가지 생각나는 문제이다.
1. 매 라운드마다 정렬을 한 뒤 제일 작은 수 2개를 빼서 연산을 가한 뒤 재정렬
2. 애초에 우선순위큐를 사용해서 라운드 돌리기

첫번째 방법의 시간복잡도는 O(m * n * log n)
두번째 방법의 시간복잡도는 O(m * log n) 으로 거의 비슷하긴하다만

우선순위큐를 사용하는편이 더 효율적이라고 볼 수 있다.

"""

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = []
for data in list(map(int, input().split())):
    heappush(cards, data)

for _ in range(m):
    first, second = heappop(cards), heappop(cards)
    heappush(cards, first + second)
    heappush(cards, first + second)

print(sum(cards))