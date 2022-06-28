"""

백준 문제 13413번 그리디_오셀로 재배치

그리디 문제중에서 그렇게 어려운 문제는 아닌데,
풀려면 재미가 있는 문제이다.

이 문제의 포인트는 B, W 서로 교환하면 어긋난거 2개가 한번에 고쳐진다는 점이다.
그 부분을 잘 생각해서 문제를 풀면된다.

결국에는 연산이 (max(black, white) - min(black, white)) + min(black, white) 라서
max(black, white)가 된다.

"""

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    before, after = input().rstrip(), input().rstrip()
    diff, black, white = [], 0, 0

    for i in range(n):
        if before[i] != after[i]:
            if before[i] == 'B':
                black += 1
            else:
                white += 1
    print(max(black, white))