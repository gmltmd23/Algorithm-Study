"""

문제 11726 2xn 타일링

DP의 원리를 알면 어려운 문제는 아닌데 정답률이 왜 낮은지는 모르겠다.
나처럼 재귀함수로 풀면 recursion depth가 깊어지기 때문에, default로 설정되있는 recursion limit으로는 풀수가 없고
sys.setrecursionlimit을 설정 해줘야만 런타임 에러가 안나고 풀수있다.

"""

import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def get_rectangle(n):
    if n <= 2:
        rectangle[n] = n
        return rectangle[n]
    if rectangle[n] == 0:
        rectangle[n] = get_rectangle(n - 1) + get_rectangle(n - 2)
    return rectangle[n]

n = int(input().rstrip())
rectangle = [0] * (n + 1)
print(get_rectangle(n) % 10007)