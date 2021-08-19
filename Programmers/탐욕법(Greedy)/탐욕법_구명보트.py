"""

프로그래머스 탐욕법(Greedy)_구명보트 : LEVEL 2

문제를 잘 읽자.. 문제에 구명보트에 탈수있는 사람은 *최대 2명* 이다...
이걸 대충읽어서 엄청 헷갈렸네ㅋㅋㅋㅋㅋㅋ

저걸 다시읽으니깐 3분만에 풀어버린 문제
내림차순 정렬때리고, 가장 무거운 사람이 가장 가벼운 사람과 같이 보트에 태울수 있으면 태워서 보내고
아니면 가장 무거운 사람 1명만 태워서 보내는 방식으로 진행하면 해결가능

"""

from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    answer = 0

    while people:
        first = people.popleft()
        if people and first + people[-1] <= limit:
            people.pop()
        answer += 1

    return answer