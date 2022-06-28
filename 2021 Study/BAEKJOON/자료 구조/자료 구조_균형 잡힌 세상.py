"""

백준 문제 4949번 자료 구조_균형잡힌 세상

스택문제이다.
스택의 구조를 알고있으면 금방 풀 수 있는 문제인데,
조건 하나를 설정을 잘못해서 반례를 못찾아 시간이 좀 걸렸던 문제

실제 시험에서는 조건실수 하는 일 없이 복습하자.

"""

import sys
input = sys.stdin.readline

special = {'[', ']', '(', ')'}
while True:
    text = input().rstrip()
    if text == '.': break

    stack = []
    for c in text:
        if c in special:
            if stack:
                if c in {'[', '('}:
                    stack.append(c)
                else:
                    if (c == ']' and stack[-1] == '[') or (c == ')' and stack[-1] == '('):
                        stack.pop()
                    else:
                        stack.append(c)
                        break
            else:
                stack.append(c)
    print("yes" if not stack else "no")