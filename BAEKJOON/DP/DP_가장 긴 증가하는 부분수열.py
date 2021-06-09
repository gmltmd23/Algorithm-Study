"""

문제 11053 가장 긴 증가하는 부분 수열

여러번 틀려서 답을 보고 복습했었던 문제이다.

DP를 사용하는 문제인데, DP의 기초를 다지기가 좋다.
max() 함수를 이용해, count를 누적할수 있다는 중요한 개념이 있으니 반드시
복습하자.

"""


import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))