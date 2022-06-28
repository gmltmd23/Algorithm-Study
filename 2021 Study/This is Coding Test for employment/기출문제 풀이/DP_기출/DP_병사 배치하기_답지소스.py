"""

답지에 있는 소스이고, 증가하는 부분 수열을 이용해서 풀었다.

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
soldiers = list(map(int, input().split()))
soldiers.reverse() # 내림차순 문제를 뒤집어버리면 오름차순 문제가 되서 접근하기가 더 편하다.
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))