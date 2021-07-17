"""

백준 문제 2212번 센서

문제 설명이 좀 난해해서, 이해하는데 좀 걸린 문제
다른사람들의 풀이를 보고 푸니깐 풀렸다.

시간복잡도는 정렬을 사용해야 하기때문에 O(n*log n)이 나온다.

"""


import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split())))
dist = []

for i in range(1, n):
    dist.append(sensors[i] - sensors[i - 1])
dist.sort()

result = 0
for i in range(len(dist) - k + 1):
    result += dist[i]
print(result)