"""

(복습) 백준 문제 2156번 포도주 시식

dp[n]은 n번째 와인까지 따졌을때 최대 마실수 있는 양 이다.

규칙상 3잔 연속만 되면 안되니깐
전체 와인의 수(n)가 2잔이하일 경우에는 그냥 dp[2] 이런식으로 리턴해주면된다.

그리고 그 이후부터는 이 3가지 경우의 수중 가장 큰 수를 dp값에 추가를 해주면 된다.

1. 현재 와인[n]은 마시지 않고, 전 와인과 전전 와인은 마시는 경우 = dp[i - 1]
2. 전전 와인까지 마시고 현재의 와인을 마시는 경우 = dp[i - 2] + wine[i]
3. 전전전 와인까지 마시고 전 와인과 현재와인을 마시는 경우 = dp[i - 3] + wine[i - 1] + wine[i]

이 3가지의 경우를 max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])
해주면 된다.

"""

import sys
input = sys.stdin.readline

n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))
dp = [0]
dp.append(wine[1])

if n > 1:
    dp.append(wine[1] + wine[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 1]))
print(dp[n])