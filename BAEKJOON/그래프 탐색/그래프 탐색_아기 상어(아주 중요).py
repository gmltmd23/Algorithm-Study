"""

백준 문제 16236번 아기 상어

문제 제목은 귀여운데, 삼성 기출문제라 그런지
난이도는 꽤 까다롭다. 복습을 반드시하자.

기본적으로 BFS 문제인데 거기서 문제를 2번정도 더 꼬아놓았다.
보통 이제 bfs를 풀때 deque를 이용해서 popleft를 계속 해주는데

계속 원소가 추가되는 deque에서 한정된 범위로 popleft를 하고싶으면
for _ in range(len(q)): 이런식으로 범위를 제한하는 테크닉이 중요하다.

"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    area[x][y] = 0
    q, visited = deque([(x, y)]), set([(x, y)])
    second, answer = 0, 0
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    shark_size, eat_count = 2, 0
    eat_flag = False

    while q:
        q = deque(sorted(q)) # 정렬을 시킴으로써 가장 위쪽에 있는것, 만약 그게안되면 가장 왼쪽에 있는것이 1빠가 된다.
        for _ in range(len(q)): # 현재 q에 있는 원소의 개수만큼만 루프를 돌린다. (이러면 새로 추가되는거는 무시하게 만들수있다.)
            bx, by = q.popleft()
            if area[bx][by] != 0 and area[bx][by] < shark_size:
                area[bx][by] = 0
                eat_count += 1
                if eat_count == shark_size:
                    shark_size += 1
                    eat_count = 0

                q, visited = deque(), set([(bx, by)])
                eat_flag = True
                answer = second

            for i in range(4):
                nx, ny = (bx + dx[i]), (by + dy[i])
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    if area[nx][ny] <= shark_size:
                        q.append((nx, ny))
                        visited.add((nx, ny))

            if eat_flag:
                eat_flag = False
                break
        second += 1
    return answer

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = None, None
for i in range(n):
    for j in range(n):
        if area[i][j] == 9:
            start_x, start_y = i, j
print(bfs(start_x, start_y))