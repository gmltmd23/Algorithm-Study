"""

프로그래머스 완전탐색_소수 찾기 : LEVEL 2

소수를 찾는 문제인데, 소수는 자신과 1로만 나누어지는 수를 말한다.
이 성질을 이용한다면, 제곱근을 구해서 2부터 제곱근까지로 나누어본다.
만약 모두 안나누어 떨어지면 이 수는 소수고
하나라도 나누어떨어지는게 발생하면 이 수는 소수가 아니다.

그리고 permutation을 사용하여 수를 만들기 때문에, 중복이 발생하기도 한다.
중복은 set으로 없애주면 효율적이니 없애고, for문을 돌려주면 더빠르게 돌릴수가 있음.

"""

from itertools import permutations
from math import sqrt

def findPrimeNumber(number):
    k = sqrt(number)
    if number < 2:
        return False

    for i in range(2, int(k) + 1):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        permu = list(map(''.join, permutations(numbers, i)))
        for j in list(set(permu)):
            if findPrimeNumber(int(j)):
                answer.add(int(j))
    return len(answer)