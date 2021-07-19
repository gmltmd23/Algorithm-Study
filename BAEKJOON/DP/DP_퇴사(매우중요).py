"""

백준 문제 14501번 퇴사

대표적인 DP 문제 중 하나이다.
예전에 풀어본적이 있던거 같은데 까먹어서 또 틀렸다..
다시 복습을 하자.

우선 나는 배열을 역순으로 접근해야한다는것 까지는 알아챘는데,
그 이후 DP 점화식을 만드는것에 실패하였다.

(day + time[day]) > n 이 조건을 만드는것 까지는 도달은 했었는데
그 이후를 못하겠어서 더 고민하다가 결국에는 인터넷 풀이를 참조했다.

풀이를 보니 2가지를 비교해서 dp값을 더해주는데,
1. 그전까지 진행됬던 dp
2. 현재 day에 있는 cost와 이 cost가 time동안 진행됬을때에 dp값

저 두가지를 비교해서 더 큰것이 dp값이 되면된다.
그럼 시간복잡도 O(n)으로 끝낼 수 있다.

"""

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
time, cost = [], []
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    cost.append(p)

for day in range(n - 1, -1, -1):
    if (day + time[day]) > n:
        dp[day] = dp[day + 1]
    else:
        dp[day] = max(dp[day + 1], cost[day] + dp[day + time[day]])
print(dp[0])