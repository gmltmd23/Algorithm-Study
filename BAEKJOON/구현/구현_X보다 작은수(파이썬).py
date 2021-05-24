"""

문제 10871 X보다 작은 수

자바로 풀었던거를 파이썬으로 풀어봤다.
코드 진짜 짧아진다.

"""

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
for number in list(map(int, input().split())):
    if number < x: print(number, end = ' ')