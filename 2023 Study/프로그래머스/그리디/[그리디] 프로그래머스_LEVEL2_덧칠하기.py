from collections import deque

def solution(n, m, section):
    if m == 1:
        return len(section)

    answer = 0
    q = deque()
    for eachSection in section:
        if not q:
            q.append(eachSection)
        else:
            frontSection = q[0]
            if (eachSection - frontSection + 1) <= m:
                q.append(eachSection)
            else:
                answer += 1
                q.clear()
                q.append(eachSection)

    if q:
        answer += 1

    return answer

n = 4
m = 4
section = [1, 3]
print(solution(n, m, section))