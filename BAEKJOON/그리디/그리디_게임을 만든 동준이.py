"""

백준 문제 2847번 게임을 만든 동준이

그리디문제중에 비교적 쉬운 문제였다.
시간복잡도를 O(n)으로 푸는것이 핵심인 문제이다.

levels 배열을 정렬없이 오름차순으로 만들어주는것과 같은 문제이다.

"""

import sys
input = sys.stdin.readline

n = int(input())
result, levels = 0, []
for _ in range(n):
    levels.append(int(input()))
base = levels[-1] - 1

for i in range(len(levels) - 2, -1, -1):
    if levels[i] > base:
        result += (levels[i] - base)
    elif levels[i] < base:
        base = levels[i]
    base -= 1
print(result)