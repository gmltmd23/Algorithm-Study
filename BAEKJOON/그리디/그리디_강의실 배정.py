"""

백준 문제 11000번 그리디_강의실 배정

정답률 29.158%의 문제이다.
그렇게까지 어려운 문제는 아닌데 내가 풀은 방법보다 시간이 더 적게 걸리는 방법이
존재할 것 같은 문제이다.

내가 짠 코드의 시간 효율성은
O(2n * log n) + O(n * log n) = O(n * log n)이다.
시간 효율성은 이것보다 크게 개선시키는 방법은 없을터이다.
room에 넣기전에 s,t를 일단 배열로 정렬해야하므로..
정렬에서만 O(n * log n)을 사용한다.

이걸 자바로도 풀어봐야겠다.
자바에서는 heapq가 PriorityQueue가 되고,
sort는 Collections.sort()를 사용해야 할듯하다.

"""

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
time = []
for i in range(n):
    s, t = map(int, input().split())
    time.append((s, t))
time.sort(key=lambda x: (x[0], x[1]))

room = []
heappush(room, time[0][1])
for i in range(1, n):
    s, t = time[i]
    if s >= room[0]:
        heappop(room)
    heappush(room, t)

print(len(room))