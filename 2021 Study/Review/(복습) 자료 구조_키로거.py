"""

(복습) 백준 문제 5397번 자료 구조_키로거

알고리즘 문제들 중에서 자료구조 문제가 나오면,
스택을 2개를 쓴다거나 큐를 2개를 쓴다거나 우선순위큐를 2개를 쓴다거나 등등..

우리가 기존에 알고있던 자료구조를 여러개 또는 다양하게 활용하게끔 문제가 나온다.
스택의 성질을 잘 알고있다면 크게 어렵지 않게 풀수있던 문제였다.

"""

import sys
input = sys.stdin.readline

special = {'<', '>', '-'}
for _ in range(int(input())):
    password, save = [], []
    origin = list(input().rstrip())
    for element in origin:
        if element in special:
            if element == '<' and password:
                save.append(password.pop())
            elif element == '>' and save:
                password.append(save.pop())
            elif element == '-':
                if save and password:
                    password.pop()
                elif not save and password:
                    password.pop()
        else:
            password.append(element)
    while save:
        password.append(save.pop())

    for c in password:
        print(c, end = '')
    print()