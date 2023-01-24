from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(sorted(people))

    while q:
        left = q.popleft()
        right = q.pop() if q else 0
        while (left + right) > limit:
            answer += 1
            right = q.pop() if q else 0
        answer += 1

    return answer

people = [20, 40, 60, 90]
limit = 100
print(solution(people, limit))