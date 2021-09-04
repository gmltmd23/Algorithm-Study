"""

프로그래머스 스택/큐(2017 팁스타운)_짝지어 제거하기 : LEVEL 2

스택문제였다. 단순하게 스택에 문자를 넣으면서 같으면 스택에서 뺴주고
아니면 넣어주면 된다. 이후 stack의 상태를 보고 정답을 결정하면 된다.

"""

def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    return 0 if stack else 1