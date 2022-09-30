def solution(s):
    answer = 1
    for start in range(len(s)):
        for end in range(start + 2, len(s) + 1):
            a = s[start:end]
            if len(a) < answer:
                continue
            if a == a[::-1]:
                answer = max(answer, end - start)
    return answer

s = "abbcbc"
print(solution(s))