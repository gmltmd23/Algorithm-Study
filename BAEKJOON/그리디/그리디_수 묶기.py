"""

일단 아래의 풀이로 계속 풀어봤는데 힙으로도 풀어보고 정렬로도 이렇게 바꿔서 풀어봤는데도,
계속 답이 틀렸었다. 뭔가 빼먹고 있는 조건이 있는거같은데..



import sys
input = sys.stdin.readline

def calc_total(numbers):
    total = 0
    while numbers:
        if len(numbers) > 1:
            total += (numbers.pop() * numbers.pop())
        else:
            total += numbers.pop()
    return total

def main():
    n = int(input().rstrip())
    minus_numbers, plus_numbers = [], []
    for i in range(n):
        num = int(input().rstrip())
        if num <= 0: minus_numbers.append(num)  # 얘는 음수가 붙어있어서 자동으로 최대힙처럼 쓸수있다.
        else: plus_numbers.append(num)  # 최대힙으로 만들기위해
    minus_numbers.sort(reverse = True)
    plus_numbers.sort()

    print(calc_total(minus_numbers) + calc_total(plus_numbers))

main()

"""


"""

문제 1744 수 묶기

계속 틀렸던 이유가 plus_numbers 리스트에서 second가 1이 나올경우였다.
first가 무엇이든간에 second가 1 이라면 first * second = first이다.
그렇지만 first + second = first + 1 과 같으므로 (first + second) > (first * second) 였던것이다.
이것을 빼먹어서 계속 틀렸던것이다 ㅠㅠ

그래도 맞췄으니 기분이 좋다.
정렬로 풀어서 68ms가 걸렸는데, 힙으로도 한번 풀어봐야겠다.

-> 힙으로도 한번 다시 풀어봤는데 힙으로 푸니깐 메모리도 더 많이 쓰고 속도도 84ms가 걸려서 더 느려졌다.
아무래도 heapify 하니깐, 그만큼 늦어진거같다.

이 문제는 정렬로 푸는게 최적이다.

"""

import sys
input = sys.stdin.readline

def calc_total(numbers):
    total = 0
    while numbers:
        if len(numbers) > 1:
            first, second = numbers.pop(), numbers.pop()
            if second == 1:
                total += (first + second)
            else:
                total += (first * second)
        else:
            total += numbers.pop()
    return total

def main():
    n = int(input().rstrip())
    minus_numbers, plus_numbers = [], []
    for i in range(n):
        num = int(input().rstrip())
        if num <= 0: minus_numbers.append(num)  # 얘는 음수가 붙어있어서 자동으로 최대힙처럼 쓸수있다.
        else: plus_numbers.append(num)  # 최대힙으로 만들기위해
    minus_numbers.sort(reverse = True)
    plus_numbers.sort()

    print(calc_total(minus_numbers) + calc_total(plus_numbers))

main()