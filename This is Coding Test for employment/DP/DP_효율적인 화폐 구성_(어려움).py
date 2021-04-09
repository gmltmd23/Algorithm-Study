import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

"""
문제 자체가 이해가 어렵다.
까다로운 문제인데 점화식을 구하는게 논점이다.
아직 이해가 잘안된다.
dp[i] = dp[i - 2] + 1 이게 중요한 점화식
"""

n, m = map(int ,input().split())
dp = [10001] * (m + 1) # 계산할수 없는 가치일경우에는 10001로 초기화
currents = []
for i in range(n):
    currents.append(int(input()))
dp[0] = 0

for i in range(n):
    for j in range(currents[i], m + 1):
        if dp[j - currents[i]] != 10001:
            dp[j] = min(dp[j], dp[j - currents[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])