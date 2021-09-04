"""

프로그래머스 위클리 1주차_부족한 금액 계산하기

1주차 문제라 그런지 그냥 풀라고 주는 이벤트문제이다.
나처럼 반복문 써서 풀어도되고, 등차수열의 합을 이용해서 풀어도 풀릴듯한다.
등차수열써서 풀었으면 아마 코드 한줄이면 풀렸을듯 하다.

"""

def solution(price, money, count):
    total = 0
    for i in range(1, count + 1):
        total += (price * i)
    return (total - money) if total > money else 0