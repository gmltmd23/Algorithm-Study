"""

프로그래머스 위클리 4주차 _ 직업군 추천하기

실제 코딩테스트에서 잘 나오는 구현문제이다.
1번문제같은걸로 많이 나오는 문제, 쉽게 풀수있지만
긴장하고 당황해버리면 시간을 잡아먹기 좋은 문제이다.

이런거를 많이 풀어서 빨리 풀수있게끔 연습하는게 중요하다.
아래 코드에서 sort로 정렬해서 풀수있겠지만, heapq로 풀어도된다.
그럼 아마 코드자체는 더 깔끔하게 나올듯

"""

def solution(table, languages, preference):
    answer, jobs = '', {}
    for line in table:
        t = line.split()
        jobs[t[0]] = {}
        score = 5
        for i in range(1, len(t)):
            jobs[t[0]][t[i]] = score
            score -= 1

    temp, result = [], []
    for job in jobs:
        score = 0
        for i in range(len(languages)):
            if languages[i] in jobs[job]:
                score += (preference[i] * jobs[job][languages[i]])
        if score:
            temp.append((score, job))
    temp.sort()

    sc, j = temp.pop()
    result.append(j)
    while temp and sc == temp[-1][0]:
        result.append(temp.pop()[1])

    return sorted(result)[0]