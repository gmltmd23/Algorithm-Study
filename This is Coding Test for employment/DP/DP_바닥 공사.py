import sys
sys.setrecursionlimit(10 ** 6) # 알고리즘 할때 안까먹기위해서 한번씩 넣어주는중
input = sys.stdin.readline

n = int(input())

"""
dp[1] = 1 (b만 들감)
dp[2] = 3 (aa, bb, c)
dp[3] = 5 (aab, baa, bc, cb, bbb)
dp[4] = 11개 (aabb, bbaa, baab, aaaa, bbbb, bbc, cbb, bcb, aac, caa, cc)

이렇게 손으로 해보면 점화식을 발견할수있다.
dp[i] = dp[i - 1] + (dp[i - 2] * 2)
이걸 이용해서 코드를 짜면 된다.
"""

dp = [0] * 1000
dp[1], dp[2] = 1, 3
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + (dp[i - 2] * 2)) % 796796 # 문제에서 796796으로 나눈 나머지를 구하라고 하길래..
print(dp[n])