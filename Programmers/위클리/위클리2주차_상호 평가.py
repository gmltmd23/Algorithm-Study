"""

프로그래머스 위클리 2주차_상호 평가

쉬운 구현 문제이다.
문제의 조건에 맞게 풀기만 하면 풀린다.
다만 중간에 최저점, 최고점을 계산할때에는 sort를 사용해도 좋고 heapq를 써도될것같지만
sort가 더 효율적이다.

"""

def give_grade(avg):
    if avg >= 90:
        return 'A'
    elif 80 <= avg < 90:
        return 'B'
    elif 70 <= avg < 80:
        return 'C'
    elif 50 <= avg < 70:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''

    for y in range(len(scores)):
        total, temp = 0, []
        for x in range(len(scores)):
            if x == y:
                me = scores[x][y]
            temp.append(scores[x][y])
        temp.sort()

        if me == temp[0] and me != temp[1]:
            answer += give_grade(sum(temp[1:]) // (len(temp) - 1))
        elif me == temp[-1] and me != temp[-2]:
            answer += give_grade(sum(temp[:len(temp) - 1]) // (len(temp) - 1))
        else:
            answer += give_grade(sum(temp) // len(temp))

    return answer

a = [[70,49,90],[68,50,38],[73,31,100]]
print(solution(a))