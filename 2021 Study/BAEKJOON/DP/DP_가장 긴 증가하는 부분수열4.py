"""

백준 14002 가장 긴 증가하는 부분 수열 4

아마 이게 답이 맞을텐데 왜 틀리다고 나오지..?

일단 LIS(Longest Increasing Subsequence)문제 같은경우에는
DP로 푸는 방법, 이진탐색으로 푸는 방법이 있는데

아래 방법은 DP로 풀은 방법이다.
DP로 풀면 시간복잡도는 O(n^2)이고, 이진탐색으로 풀면 O(nlog n) 이다.

왜 계속 틀리다고 나오는지 이해가 안간다.
문제에 조건이 추가가 됬나..?

"""


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
maxDP = 0

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > maxDP:
                maxDP = dp[i]
print(maxDP)
result = []
for i in range(n - 1, -1, -1):
    if maxDP == dp[i]:
        result.append(arr[i])
        maxDP -= 1
print(*reversed(result))