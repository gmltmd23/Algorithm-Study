"""

문제 2110 공유기 설치

문제 설명 자체가 좀 애매해서, 이해하기 난해했던 문제,
일단 기본적으로 이진탐색을 사용하는 기본문제인것에는 변화가 없다.

"""

import sys
input = sys.stdin.readline

def main():
    n, c = map(int, input().split())
    houses = []
    for i in range(n):
        houses.append(int(input().rstrip()))
    houses.sort()

    start, end = 1, (houses[-1] - houses[0])
    result = -1
    while start <= end:
        center = (start + end) // 2
        now = houses[0]
        count = 1
        for i in range(1, n):
            if houses[i] >= now + center:
                count += 1
                now = houses[i]

        if count < c:
            end = center - 1
        else:
            start = center + 1
            result = center
    print(result)

main()