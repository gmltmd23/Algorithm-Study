"""

프로그래머스 위클리 5주차_모음 사전

문제에서 힌트를 줬다.
A의 경우 result = 1
I의 경우 result = 1563

A -> E -> I -> O -> U 순서이기때문에, A와 I는 2칸이 차이나는데
result가 1562만큼 차이난다는것은 1칸마다 781 차이라는것이다. (len(word) == 5 인 경우)

자릿수가 내려갈때마다 save에 -1을하고 5로 나눠주면된다.

계산하면 끝

"""

def solution(word):
    answer, aeiou = 0, {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U' : 4}
    save = 781
    for w in word:
        answer += 1 + save * aeiou[w]
        save = (save - 1) // 5

    return answer

print(solution("AAAAE"))