"""

백준 문제 18310번 그리디_안테나

정답률 35.993%의 문제이다.
정답률이 왜이렇게 낮지..? 어려운 문제가 아니다.

파이썬으로 풀든, 자바로 풀든, C++로 풀든 정렬을 하겠다는 생각을 하면 금방 풀 수 있는 문제였다.

"""

import sys
input = sys.stdin.readline

n = int(input())
houses = sorted(list(map(int, input().split())))
print(houses[0] if n == 1 else houses[(n - 1) // 2])