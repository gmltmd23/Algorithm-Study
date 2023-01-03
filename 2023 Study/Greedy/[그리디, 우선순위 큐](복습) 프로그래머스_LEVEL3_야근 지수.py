from heapq import heappush, heappop

def solution(n, works):
    q = []
    for work in works:
        heappush(q, -work)

    for i in range(n):
        if not q:
            break
        value = heappop(q) + 1
        if value != 0:
            heappush(q, value)

    return sum(map(lambda x: x ** 2, q))


n = 4
works = [4, 3, 3]
print(solution(n, works))