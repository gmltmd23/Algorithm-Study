"""

백준 문제 11501번 그리디_주식

정답률 33.873%의 문제이다.
이 문제에서 할 수 있는 행동은 3가지이다.
1. 주식을 사거나
2. 몽땅 팔거나
3. 아무것도 안하거나

그런데 굳이 그렇게 3개로 나눠서 생각 할 필요는 없고
주식을 사서 가장 이득을 볼때 팔면된다.

고로 배열을 역순으로 보면서 maximum 값을 정한다.
초기 maximum값보다 작은 원소라면 profit에 (maximum - stocks[i])를 더해주고,
maximum값보다 큰 것이 존재한다면 maximum = stocks[i]를 해주면된다.

그러면 쉽게 진행 할 수 있다.
시간복잡도는 원래 O(n)이 나오는 문제이지만
테스트케이스 t로 여러개를 주어주기 때문에 O(t * n)이 된다.

"""

import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    stocks = list(map(int, input().split()))
    profit, maximum = 0, 0
    for i in range(n - 1, -1, -1):
        if stocks[i] <= maximum:
            profit += maximum - stocks[i]
        else:
            maximum = stocks[i]
    print(profit)