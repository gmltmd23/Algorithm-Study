def getAlphabetOrLeftover(leftover):
    if leftover == '10': return 'A'
    elif leftover == '11': return 'B'
    elif leftover == '12': return 'C'
    elif leftover == '13': return 'D'
    elif leftover == '14': return 'E'
    elif leftover == '15': return 'F'
    else: return leftover

def nJinsu(number, N):
    if number == 0:
        return '0'

    stack = []
    while number > 1:
        stack.append(getAlphabetOrLeftover(str(number % N)))
        number //= N
    if number != 0:
        stack.append(str(number))

    return ''.join(stack[::-1])

def solution(n, t, m, p):
    targetString, number = '', 0
    while len(targetString) <= (t * m):
        targetString += nJinsu(number, n)
        number += 1

    answer = ''
    for i in range((p - 1), len(targetString), m):
        if len(answer) >= t:
            break
        answer += targetString[i]

    return answer

n, t, m, p = 16, 16, 2, 1
print(solution(n, t, m, p))