"""

프로그래머스 해시 문제 : 완주하지 못한 선수

내가 해시쪽에 문제가 약했나보다, 더 연습해야겠다.
우선 딕셔너리를 사용해서 카운팅해주는 방식으로 문제를 해결하였고,

그 결과 시간복잡도 O(n + n + n) = O(n)으로 해결할수 있었다.

"""

def solution(participant, completion):
    temp = {}
    for person in participant:
        if person not in temp:
            temp[person] = 1
        else:
            temp[person] += 1

    for com in completion:
        temp[com] -= 1

    for key in temp.keys():
        if temp[key] > 0:
            return key

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))