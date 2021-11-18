"""

백준 문제 2573번 그래프 탐색_빙산

정답률 25%의 문제이다.
메모리문제가 발생할수도 있으므로 dfs보다는 bfs로 푸는것을 권장한다.
내가 풀은 방식으로는 아마 melt()함수에 들어가서 check()함수를 호출 하기에
최악의경우에 시간복잡도가 좋지않게 나와서 컴파일러가
Python3으로 하게되면 시간초과가 나오게되서 pypy로 제출해보니 성공했다.

melt()함수 하나로 끝내는 방법이 생각이 나긴나는데, 나중에 시간날때 해봐야겠다.
전체 배열(N x M)을 풀스캔하지않고 빙하가 있는 지역만 골라내서 그 부분만 반복문을 돌리는게 핵심인 문제였다.

"""

from collections import deque
import sys
input = sys.stdin.readline

def check():
    save = ice.copy()
    q = deque([save.pop()])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) in save:
                    save.remove((nx, ny))
                    q.append((nx, ny))

    return True if save else False

def melt():
    global ice
    year = 0
    while ice:
        minus = set()
        for x, y in ice:
            for i in range(4):
                nx, ny = (x + dx[i]), (y + dy[i])
                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) not in ice and graph[nx][ny] == 0:
                        if graph[x][y] != 0:
                            graph[x][y] -= 1
                        if graph[x][y] == 0:
                            minus.add((x, y))
        year += 1
        ice = (ice - minus)

        if not ice:
            return 0
        if check():
            return year

n, m = map(int, input().split())
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
graph = [[] for _ in range(n)]
ice = set()
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        graph[i].append(line[j])
        if line[j] != 0:
            ice.add((i, j))
print(melt())