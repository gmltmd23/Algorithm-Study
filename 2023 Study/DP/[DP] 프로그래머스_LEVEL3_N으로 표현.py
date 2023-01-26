def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(10)]
    for i in range(1, 10):
        dp[i].add(int(str(N) * i))

    for i in range(2, 9):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2:
                        dp[i].add(num1 // num2)
        if number in dp[i]:
            return i

    return -1

N = 5
number = 12
print(solution(N, number))