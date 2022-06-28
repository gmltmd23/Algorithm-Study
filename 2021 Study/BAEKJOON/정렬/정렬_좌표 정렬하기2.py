"""

백준 정렬_좌표 정렬하기2

가벼운 정렬문제였다. 우선 y축 기준으로 오름차순 정렬한 뒤
그 다음 x축 기준으로 오름차순 정렬해주면 끝나는 문제

"""

import sys
input = sys.stdin.readline

n = int(input())
pos = []
for i in range(n):
    pos.append(list(map(int, input().split())))
for x, y in sorted(pos, key=lambda x: (x[1], x[0])):
    print(x, y)