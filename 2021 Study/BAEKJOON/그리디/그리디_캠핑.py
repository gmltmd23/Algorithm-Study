"""

답 자체는 금방 맞췄는데, 문제 설명이 뭔가 난해해서 애매했던 문제
이 문제의 포인트는 min((v % p), l) 이것이다.
min() 함수를 사용하지않고, 그냥 v % p을 대입해버리면 답이 틀린다.

"""

import sys
input = sys.stdin.readline

case = 1
while True:
    l, p, v = map(int, input().split())
    if l + p + v == 0: break
    print(f'Case {case}: {((v // p) * l) + min((v % p), l)}')
    case += 1