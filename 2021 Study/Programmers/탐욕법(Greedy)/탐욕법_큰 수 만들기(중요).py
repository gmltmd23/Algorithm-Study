"""

프로그래머스 탐욕법(Greedy)_큰 수 만들기 : LEVEL 2

레벨 2 문제인데, 다른 레벨2보다는 난이도가 있던 문제였다.
스택과 그리디기법을 함께 활용하는 문제였다.

마지막에 return을 슬라이싱한 범위에 있는 stack으로 하는 이유는
number = "999", k = 2 인 경우 때문에 그렇다.
이거는 답이 9가 나와야되는데, 저 로직상 999가 나온다.
그래서 저렇게 리턴해주는것이다.


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