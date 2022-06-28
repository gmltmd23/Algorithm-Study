"""

백준 문제 1041번 주사위

그리디 문제이고, 아이디어 자체는 머리에 금방 떠오른 문제이긴한데
sumList를 만드는것이 잘 떠오르지 않아
sumList쪽만 인터넷을 참고하였다.

정답률은 낮지만 난이도는 방법만 알면 그리 안높은 문제였다.

"""

import sys
input = sys.stdin.readline

def solution(n, dice):
    if n == 1:
        return sum(dice) - max(dice)
    else:
        sumList = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
        sumList.sort()
        one = ((n - 2) * (n - 2)) + (n - 1) * (n - 2) * 4
        two = ((n - 2) * 4) + (n - 1) * 4
        three = 4
        return one * sumList[0] + two * sum(sumList[:2]) + three * sum(sumList)

n = int(input())
dice = list(map(int, input().split()))
print(solution(n, dice))