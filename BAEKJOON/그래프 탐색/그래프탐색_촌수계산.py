"""

백준 문제 2644번 촌수계산

처음에는 find_parent를 사용해서 푸는문제인줄 알고 풀었다.
그런데 다풀고 제출하니깐 16%정도 통과했을때쯤
런타임에러(TypeError)가 발생한다.

아마도 내가 체크못한 경우의 수가 한두가지가 있었나보다.
그럴수밖에 없는게 내가 짠 코드는 n == 1일때는 동작하지 않는 코드이기 때문에,
함수들에서 None들을 반환했나보다

그래서 자세한 풀이가 알고싶어 인터넷을 참고하니,
사람들은 bfs또는 dfs를 활용하여 풀었다.

복습해두자.

import sys
input = sys.stdin.readline

def find_parent(parent, x, res):
    if parent[x] != x:
        res.append(parent[x])
        parent[x] = find_parent(parent, parent[x], res)
    return res

def solution(res_a, res_b):
    for i in range(len(res_a)):
        for j in range(len(res_b)):
            if res_a[i] == res_b[j]:
                return (i + 1) + (j + 1)
    return -1

n = int(input())
parent = [_ for _ in range(n + 1)]
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    parent[y] = x
res_a, res_b = [], []
print(solution(find_parent(parent, a, res_a), find_parent(parent, b, res_b)))

"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    q = deque()
    q.append(node)
    while q:
        target = q.popleft()
        for next_node in graph[target]:
            if check[next_node] == 0:
                check[next_node] = check[target] + 1
                q.append(next_node)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
bfs(a)
print(check[b] if check[b] > 0 else -1)