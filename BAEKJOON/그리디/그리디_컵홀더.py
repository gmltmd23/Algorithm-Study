"""

백준 문제 2810번 컵홀더

다 풀고보니깐 그렇게 어려운 문제는 아니었는데, 중간에 생각이 한번 꼬여서
푸는데 좀 걸렸던 문제이다.

코드를 더 예쁘게 줄일수 있을거같긴한데, 그렇다고해도 아래 코드 자체 시간복잡도가 O(n)으로
이보다 더 처리속도가 개선되지는 않을테니
문제는 여기까지만 풀어야겠다.

"""

import sys
input = sys.stdin.readline

def solution(n, seats):
    if seats[0] == 'S':
        cups = 2
        couple = False
    else:
        cups = 1
        couple = True

    for i in range(1, n):
        if seats[i] == 'S':
            cups += 1
        else:
            if couple:
                cups += 1
                couple = False
            else:
                couple = True

    return cups if cups < n else n

n = int(input())
seats = input().rstrip()
print(solution(n, seats))