"""

백준 문제 1759번 백트래킹_암호 만들기

브루트포스 겸 백트래킹 문제이다.
정답률은 44.917% 이다.

재귀조건을 따져가며 문제를 이어가야 하기때문에 처음에 구상할때는 머리가 약간 아픈문제,
파이썬을 이용한다면 itertools의 permutations를 이용해서 풀 수도 있을것같지만
이런식으로 풀라고 낸 문제이기 때문에 백트래킹을 사용하는 재귀 방식으로 풀어봤다.

과정을 잘 거슬러 올라가며, 신중하게 짜야하기 때문에 사고력을 키우는데 도움을 주는 좋은 문제이다.

"""

import sys
input = sys.stdin.readline

def check_code(code):
    mo, ja = False, 0
    for element in code:
        if element in ('a', 'e', 'i', 'o', 'u'):
            mo = True
        else:
            ja += 1
    if mo and ja >= 2:
        return True
    return False

def get_code(alphabets, idx, l, temp, answer):
    if len(temp) == l:
        if check_code(temp):
            print(temp)
        return

    for i in range(idx, len(alphabets)):
        get_code(alphabets, i + 1, l, temp + alphabets[i], answer)

def main():
    l, c = map(int, input().split())
    alphabets = list(input().split())
    alphabets.sort()

    answer = []
    get_code(alphabets, 0, l, "", answer)

main()