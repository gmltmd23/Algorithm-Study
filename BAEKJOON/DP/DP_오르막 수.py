"""

백준 문제 11057번 DP_오르막 수

DP 문제이다.
수의 개수가 1인 수는 무조건 오르막 수 이니깐 기본세팅을
dp = [1] * 10 이걸로 해놓는다.

그리고 예를들어 n = 2 라면
dp 배열로 dp를 시작하면 된다.

dp[0]은 끝자리의 수가 0일때 앞에 올수 있는 애들의 개수를 뜻한다.
끝자리가 0이라면 앞에는 0밖에 못오니깐 dp[0] = 1은 항상 일정하다.

이제 dp[1]부터가 중요한데, 끝자리에 1을 둘수있는 아이는 0 또는 1이다.
즉 dp[1] = dp[1] + dp[0] 이렇게 된다.
그러면 연쇄적으로 dp[2] = dp[2] + dp[1] 이렇게 된다.

결론적으로 나온 DP 점화식은
dp[j] += dp[j - 1] 이다.

중요하니 복습하자

"""

n = int(input())
dp = [1] * 10

for i in range(n - 1):
    for j in range(1, len(dp)):
        dp[j] += dp[j - 1]
print(sum(dp) % 10007)