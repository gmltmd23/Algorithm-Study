"""

백준 문제 2720번 세탁소 사장 동혁

문제 설명이 재밌어서 풀었다ㅋㅋㅋㅋㅋ
그리디문제에 있어서 기초중의 기초인 거스름돈 문제이다.

함수로 풀어서, 코드가 아름답게 나와 만족한다.
람다로 풀어볼까 했는데, 그럼 오히려 코드가 더 안예쁘게 나올거같아서 여기서 만족

"""

import sys
input = sys.stdin.readline

def make_change(change, unit):
    mok = change // unit
    print(mok if mok > 0 else 0, end = ' ')
    return change - (unit * mok)

for case in range(int(input())):
    change = int(input())

    change = make_change(change, 25)
    change = make_change(change, 10)
    change = make_change(change, 5)
    change = make_change(change, 1)
    print()
