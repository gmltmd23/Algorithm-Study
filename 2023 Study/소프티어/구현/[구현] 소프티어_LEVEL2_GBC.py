import sys
input = sys.stdin.readline

n, m = map(int, input().split())
way = [0] * 101
nowPosition = 1
for _ in range(n):
    distance, speed = map(int, input().split())
    for i in range(nowPosition, nowPosition + distance):
        way[i] = speed
    nowPosition += distance

nowPosition = 1
for _ in range(m):
    distance, speed = map(int, input().split())
    for i in range(nowPosition, nowPosition + distance):
        way[i] = speed - way[i]
    nowPosition += distance

answer = max(way[1:])

print(0 if answer <= 0 else answer)