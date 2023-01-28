def hanoi(answer, n, a, b, c):
    if n == 1:
        answer.append([a, c])
    else:
        hanoi(answer, n - 1, a, c, b)
        answer.append([a, c])
        hanoi(answer, n - 1, b, a, c)

def solution(n):
    answer = []
    hanoi(answer, n, 1, 2, 3)
    return answer

n = 3
print(solution(n))