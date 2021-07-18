"""

백준 문제 14659번 한조서열정리하고옴ㅋㅋ

그리디 문제이기도 하면서, DP문제이기도 한 문제같다.
그냥 브루트포스 방식으로하면 시간복잡도 O(n^2)로 쉽게 풀수는 있지만
당연히 그러면 시간초과가 발생하여 문제가 틀린다.

그럼 정렬을 사용해서 O(n*log n)으로 풀거나,
아니면 다른 트릭을 발견해서 O(n)정도로 풀라는 문제인데..

생각을 해보니깐 비교를 해주면서 dp에 기록을하고,
그리고 비교를하면 서로 위치를 바꿔주며, 대상을 끌어올려주는 방식을 사용했다.

그러면 반복문이 이중으로 돌 필요없이 반복문 한개로 끝낼수가 있다.

"""


import sys
input = sys.stdin.readline

n = int(input())
hanjo = list(map(int, input().split()))
dp = [0] * n
max_number = 0

for i in range(1, n):
    if hanjo[i] < hanjo[i - 1]:
        dp[i] += (dp[i - 1] + 1)
        hanjo[i], hanjo[i - 1] = hanjo[i - 1], hanjo[i]
    if max_number < dp[i]:
        max_number = dp[i]
print(max_number)