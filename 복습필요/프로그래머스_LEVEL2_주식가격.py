def solution(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(len(prices) - (i + 1))
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer[-1] -= (len(prices) - j - 1)
                break

    return answer

prices = [2, 3, 4, 5, 4, 3, 1]
print(solution(prices))