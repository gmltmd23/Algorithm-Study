"""

백준 1912번 연속합

이 문제의 핵심은 시간복잡도를 O(n)으로 푸는것이 핵심이다. (대다수의 DP문제가 그렇긴하다만..)
그 의미는 sort 같은거 쓰지말고, 저 배열 자체에서 한큐에 끝내라는 의미이다.

1~2번 해보니깐 금방 규칙을 찾아서 금방 풀수있던 DP 문제였다.
배열 옆칸들의 요소들을 더하다가 더한 값이 자신보다 크면 dp에 저장하고,
그렇지 않으면 dp에는 그냥 자기자신을 저장하는 방법이면 쉽게 풀린다.

"""

import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    numbers = list(map(int, input().split()))
    dp = numbers[:]
    result = dp[0]
    for i in range(1, n):
        data = dp[i - 1] + numbers[i]
        if data > numbers[i]:
            dp[i] = data
        if dp[i] > result:
            result = dp[i]
    print(result)
main()