"""

알고싶어.. 너의 RGB값..

문제 1149 RGB거리

정답률은 높지만 꽤 까다로운 문제였었다.
문제의 조건인 2 <= n 을 자세히봤었으면 힌트가 됬었겠지만,
밑에 방법을 잘 못떠올렸었다.

그래서 블로그같은곳을 참고해서 힌트를 얻고 만들으니 금방 풀렸다.
이거는 복습을 해야하는 문제이다.

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
rgb = []
for i in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1, n):
    rgb[i][0] += min(rgb[i - 1][1], rgb[i - 1][2])
    rgb[i][1] += min(rgb[i - 1][0], rgb[i - 1][2])
    rgb[i][2] += min(rgb[i - 1][0], rgb[i - 1][1])

print(min(rgb[-1]))