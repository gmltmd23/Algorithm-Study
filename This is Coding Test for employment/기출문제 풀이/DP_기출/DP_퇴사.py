"""

뒤에서부터 보면 더 효율적이게 DP 코드를 짤수가있다.
답지를 참고하면서 개선을 했는데, 이것저것 고민해보면 이게 가장 효율적인 방법이다.

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
time, pay = [], []
dp = [0] * (n + 1)
max_pay = 0
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

for i in range(n - 1, -1, -1):
    next = i + time[i]
    if next <= n:
        dp[i] = max(max_pay, pay[i] + dp[next])
        max_pay = dp[i]
    else:
        dp[i] = max_pay

print(max_pay)