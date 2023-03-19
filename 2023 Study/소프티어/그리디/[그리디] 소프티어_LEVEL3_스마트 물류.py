import sys
input = sys.stdin.readline

ROBOT, PART = 'P', 'H'
n, k = map(int, input().split())
lineString = input().rstrip()

answer = 0
line = list(lineString)
for i in range(n):
    if line[i] != ROBOT:
        continue
    for j in range(i - k, i + k + 1):
        if j < 0 or j >= n:
            continue
        if line[j] == PART:
            line[j] = None
            answer += 1
            break

print(answer)