"""

백준 문제 9576번 책 나눠주기

그리디문제이고, 계속 비슷한 유형이 반복되긴한다.
책을 원하는 범위중 맥시범 범위를 기준으로 정렬을 때려주고

그 이후 한개씩 번갈아가며 카운팅을 해주는 방식이다.
다른방식으로 생각해서 풀었었는데 시간초과가 나는 바람에

인터넷에서 풀이를 참고하여 풀었다. 복습하자!

"""

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    books = [True] * (n + 1)
    count = 0
    volunteer = [tuple(map(int, input().split())) for i in range(m)]
    volunteer = sorted(volunteer, key = lambda x: (x[1]))

    for a, b in volunteer:
        for i in range(a, b + 1):
            if books[i]:
                books[i] = False
                count += 1
                break
    print(count)