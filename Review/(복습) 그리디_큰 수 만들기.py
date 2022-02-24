"""

(복습) 프로그래머스 탐욕법(Greedy)_큰 수 만들기 : LEVEL 2

스택과 그리디기법을 함께 활용하는 문제였다.
마지막에 return을 슬라이싱한 범위에 있는 stack으로 하는 이유는
number = "999", k = 2 인 경우 때문에 그렇다.


"""

def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    return "".join(stack[:len(number) - k])

print(solution("999", 2))