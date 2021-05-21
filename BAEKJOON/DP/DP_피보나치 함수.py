"""

문제 1003 피보나치 함수

기존 피보나치 함수 문제를 응용한 DP 문제,
0과 1을 카운팅 해주는 배열을 따로 만들고 그것들도 DP로 돌리면 문제없이 해결 할 수 있지만
내가 짠 코드는 더 예쁘게 다듬을 여지가 있어보인다.

"""

import sys
input = sys.stdin.readline

def get_zero(n):
    if n <= 1:
        return zero[n]
    if zero[n] == 0:
        zero[n] = get_zero(n - 1) + get_zero(n - 2)
    return zero[n]

def get_one(n):
    if n <= 1:
        return one[n]
    if one[n] == 0:
        one[n] = get_one(n - 1) + get_one(n - 2)
    return one[n]

def fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if fib[n] == 0:
        fib[n] = fibonachi(n - 1) + fibonachi(n - 2)
        get_zero(n)
        get_one(n)
    return fib[n]

t = int(input().rstrip())
fib, zero, one = ([0] * 41), ([0] * 41), ([0] * 41)
fib[0], fib[1] = 0, 1
zero[0], zero[1], one[0], one[1] = 1, 0, 0, 1
for i in range(t):
    n = int(input().rstrip())
    fibonachi(n)
    print(zero[n], one[n])