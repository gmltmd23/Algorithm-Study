"""

프로그래머스 힙_디스크 컨트롤러 : LEVEL 3

힙 문제이긴 하다만 정렬을 써서 푸는게 아주 편한 문제였다.
비용순으로 정렬한뒤에 처리할수 있는 시간이 되면 바로바로 처리해주는 방법

"""

def solution(jobs):
    answer, start, length = 0, 0, len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs) - 1:
                start += 1

    return answer // length