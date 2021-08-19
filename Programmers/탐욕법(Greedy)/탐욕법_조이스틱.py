"""

프로그래머스 탐욕법(Greedy)_조이스틱 : LEVEL 2

배열에서 가장 가까운 순서에 있는(오른쪽으로든 왼쪽으로든) 요소를 먼저
바꿔주는 탐욕법 알고리즘으로 풀면 풀린다.

"""

def solution(name):
    name = list(map(str, name))
    target = ['A' for _ in range(len(name))]
    count, cursor = 0, 0

    while target != name:
        if target[cursor] == name[cursor]:
            l, r = cursor, cursor
            leftCounter, rightCounter = 0, 0

            while target[l] == name[l]:
                l -= 1
                leftCounter += 1
            while target[r % len(name)] == name[r % len(name)]:
                r += 1
                rightCounter += 1

            if leftCounter < rightCounter:
                cursor = l + len(name) if l < 0 else l
                count += leftCounter
            else:
                cursor = r % len(name)
                count += rightCounter
        else:
            count += min((ord(name[cursor]) - ord(target[cursor])), (ord('Z') - ord(name[cursor]) + 1))
            target[cursor] = name[cursor]

    return count