def solution(stones, k):
    left, right = 1, 200000000

    while left <= right:
        mid = (left + right) // 2
        resistance = 0
        for stone in stones:
            if stone < mid:
                resistance += 1
                if resistance == k:
                    break
            else:
                resistance = 0

        if resistance == k:
            right = mid - 1
        else:
            left = mid + 1

    return right


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

stones2 = [5, 4, 3, 2, 1]
k2 = 2

print(solution(stones, k))
print(solution(stones2, k2))
