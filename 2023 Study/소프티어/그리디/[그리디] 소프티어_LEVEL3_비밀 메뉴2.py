from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

difference = abs(n - m)
if n < m:
    n = m
    for _ in range(difference):
        first.append(-1)
else:
    m = n
    for _ in range(difference):
        second.append(-1)

answer = 0
leftQueue = deque()
for _ in range(n):
    leftQueue.append(0)

for loopCount in range(n):
    i, temp = 0, 0
    while i < n:
        if first[i] == second[i]:
            temp += 1
        else:
            answer = max(answer, temp)
            temp = 0
        i += 1
    if temp != 0:
        answer = max(answer, temp)
    first.append(0)
    leftQueue.popleft()
    leftQueue.append(first.popleft())

    j, leftTemp = 0, 0
    while j < n:
        if leftQueue[j] == second[j]:
            leftTemp += 1
        else:
            answer = max(answer, leftTemp)
            leftTemp = 0
        j += 1
    if leftTemp != 0:
        answer = max(answer, leftTemp)

print(answer)