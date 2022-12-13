def makeFactorial(n):
    if n < 1:
        return 1
    return n * makeFactorial(n - 1)

def solution(n, k):
    numbers = [i for i in range(1, n + 1)]
    answer = []
    while n != 0:
        divider = makeFactorial(n - 1)
        index = k // divider
        k %= divider
        if k == 0:
            answer.append(numbers.pop(index - 1))
        else:
            answer.append(numbers.pop(index))
        n -= 1

    return answer

n = 3
k = 5
print(solution(n, k))