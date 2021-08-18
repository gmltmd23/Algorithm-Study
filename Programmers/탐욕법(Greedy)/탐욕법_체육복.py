"""

프로그래머스 탐욕법(Greedy)_체육복 : LEVEL 1

이거 레벨1 문제인데 레벨2급은 되는거같다.
사고적인 전환이 필요한 문제라서 그런것 같다.

주어진 요소들을 set으로 만들고 풀면 빠르게 풀수가있다.
다만 set으로 전환할때 O(n)만큼의 시간을 이미 써버리기때문에,
이 알고리즘의 시간복잡도는 O(n) 이다.

"""

def solution(n, lost, reserve):
    reserve_set, lost_set = (set(reserve) - set(lost)), (set(lost) - set(reserve))

    for i in reserve_set:
        if (i - 1) in lost_set:
            lost_set.remove(i - 1)
        elif (i + 1) in lost_set:
            lost_set.remove(i + 1)

    return (n - len(lost_set))