"""

프로그래머스 DP_도둑질 : LEVEL 4

어려운 문제이시다..
고민을 해봤는데, 답이 안나와서 인터넷 풀이들을 참고해보았다.

역시 풀이를 알고나니깐 어려운문제가 아니다.
DP문제들은 이런것들이 너무 맘이아픔

방법은 이렇다.
DP배열을 2개를 만든다 왜냐하면..
1) 첫번째 집을 터는경우 (이 경우 맨 마지막집은 당연히 못털음) = dp1
2) 맨 마지막 집을 터는경우 (이 경우 첫번째 집을 안터는거임) = dp2

그걸 생각하고 문제를 풀면 풀린다.
dp식 같은경우에는
dp[i] = max(dp[i - 1], money[i] + dp[i - 2])
풀어서 얘기하자면 i번째 집의 dp값은 (i - 1)번째집까지 털었을때까지의 dp값 VS i번째 집이 가지고 있는 돈 + (i - 2)번째 집의 dp값
이렇게 두가지를 비교하여 큰값이 i번째 집의 dp값이 된다.
왜냐하면 연달아서 붙어있는 집 2개는 못털기 때문이다.

3일내로 반드시 복습하자.ㅈ

"""

def solution(money):
    dp1 = [0] * len(money)
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])

    dp2 = [0] * len(money)
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])

    return max(max(dp1), max(dp2))