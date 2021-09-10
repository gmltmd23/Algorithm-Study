"""

백준 문제 2828번 사과 담기 게임

문제를 제대로 안읽어서 오래걸린 문제ㅋㅋㅋㅋ

일단은 쉬운 그리디 문제이다. 바구니의 크기 M이 주어지는데
이걸로 left, right (양끝)을 만들어놓고 ball이 주어지는 위치에 따라 움직인 위치만
카운트 해주면 된다.

근데 문제를 대충 읽어가지고 바구니의 시작위치가 첫 ball의 위치로 주어지는줄 알았다.
만약 그런문제였다면 M이 1이라면 상관없지만 M이 2 이상이라면
바구니가 오른쪽으로 더 길게 놓아져야할지, 왼쪽으로 길게놓아져야할지 처음 시작하는 볼과 그 다음볼을 보고 정해야 하기때문이다.

그래서 그 방식으로 코드를 짜고 있다가, 다시 문제를 읽는도중
바구니 시작위치가 주어져있네 ^^

바구니 위치를 알게 된 이후로는 푸는데 1분정도 걸렸다..

"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())
left, right = 1, 1 + (M - 1)

count = 0
for i in range(J):
    ball = int(input())
    if ball < left:
        count += (left - ball)
        right -= (left - ball)
        left = ball
    elif ball > right:
        count += (ball - right)
        left += (ball - right)
        right = ball
print(count)