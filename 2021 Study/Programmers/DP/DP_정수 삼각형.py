"""

프로그래머스 DP_정수 삼각형 : LEVEL 3

어렵지 않은 DP 문제였다.
규칙 하나만 찾으면 금방 풀수있다.
i행j열에 있는 정수를 이용하여 (i+1)행j열, (i+1)행(j+1)열 이렇게 2개의 정수의 dp값을 계산해낼수가 있다.

저걸 반복하여 삼각형 맨 밑까지 dp행렬을 만들어준다.
그리고 맨 마지막 줄에서 max값을 얻으면 그게 답이된다.

DP문제가 이렇게만 나오면 참 좋을텐데..

"""

def solution(triangle):
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(len(dp) - 1):
        for j in range(len(dp[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
    
    return max(dp[-1])