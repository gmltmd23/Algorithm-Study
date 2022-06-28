"""

백준 문제 1931번 그리디_회의실 배정

정답률 29.128%의 그리디 문제이다.
회의실 안에 최대한 많은 회의를 진행하게끔 스케줄을 배치해주는 문제이다.

이것보다 더 빠르게 푸는 방법도 있을거 같긴한데
일단 이렇게 짜봤다, 리팩토링하면 개선될 구조는 보인다.
시간날때 한번 더 짜보자.

"""

from collections import deque
import sys
input = sys.stdin.readline

n, times = int(input()), []
for i in range(n):
    start, end = map(int, input().split())
    times.append([start, end])
times.sort()

q, idx = deque([times[0]]), 1
while idx < len(times):
    flag = False
    for i in range(idx, len(times)):
        if q[-1][1] <= times[i][0]:
            q.append(times[i])
            flag, idx = True, (i + 1)
            break
        if q[-1][0] <= times[i][0] and times[i][1] <= q[-1][1]:
            q.popleft()
            q.append(times[i])
            flag, idx = True, (i + 1)
            break
    if not flag:
        idx += 1
print(len(q))