# 구름 알고리즘 먼데이 (1주차 - 2022.10.03)

def first(): # 1번 문제 - 경로의 개수
    user_input = input()
    numbers = list(map(int, input().split()))
    answer = 1
    for element in numbers:
        answer *= element
    print(answer)

def second(): # 2번 문제 - 동명이인
    n, targetName = input().split()
    answer = 0
    for i in range(int(n)):
        if targetName in input().rstrip():
            answer += 1
    print(answer)

def third(): # 3번 문제 - 최장 맨해튼 거리
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(abs((numbers[0] - numbers[3]) + (numbers[1] - numbers[2])))

def fourth(): # 4번 문제 - 소수 찾기
    import math

    def isPrimeNumber(i):
        if i == 1:
            return False

        for divNumber in range(2, int(math.sqrt(i)) + 1):
            if i % divNumber == 0:
                return False
        return True

    n = int(input())
    numbers = list(map(int, input().split()))
    answer = 0
    for i in range(n):
        nowNumber = (i + 1)
        if isPrimeNumber(nowNumber):
            answer += numbers[i]
    print(answer)