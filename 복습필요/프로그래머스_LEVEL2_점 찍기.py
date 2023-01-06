import math

def solution(k, d):
    def solve(i):
        return math.sqrt((d * d) - (i * i))

    answer = 0
    for i in range(0, d + 1, k):
        value = solve(i)
        answer += math.floor(value / k) + 1

    return answer


k = 2
d = 4
print(solution(k, d))