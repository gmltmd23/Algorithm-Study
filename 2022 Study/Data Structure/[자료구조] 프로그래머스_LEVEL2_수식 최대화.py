from collections import deque
from itertools import permutations

def calculate(left, right, op):
    if op == '*':
        return left * right
    elif op == '+':
        return left + right
    else:
        return left - right

def process(order, expression):
    temp = ''
    q = deque()
    for element in expression:
        if element.isdigit():
            temp += element
        else:
            q.append(int(temp))
            temp = ''
            q.append(element)
    if temp != '':
        q.append(int(temp))

    for nowOp in order:
        stack = []
        while q:
            element = q.popleft()
            if nowOp == element:
                stack.append(calculate(stack.pop(), q.popleft(), nowOp))
            else:
                stack.append(element)
        q = deque(stack)

    return abs(stack[0])


def solution(expression):
    orders = permutations(('*', '+', '-'))
    answer = 0
    for order in orders:
        answer = max(answer, process(order, expression))
    return answer


expression = "100-200*300-500+20"
print(solution(expression))