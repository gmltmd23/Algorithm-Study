"""

프로그래머스 그래프_가장 먼 노드 : LEVEL 3

처음에는 dfs방식으로 1번 노드에서 출발해서, 각 노드마다 걸리는 cost를 기록해뒀다.
그렇게 cost를 기록해놓은 배열에서 max값을 찾은후 그 max값과 같은 원소의 갯수를 세는 방식으로
예시가 잘 풀리길래 제출하니깐 테스트케이스 7, 8, 9에서 계속 런타임 에러가 났다.

코드에서는 암만봐도 문제가 없었는데..
아마도 setrecursionlimit을 설정했으면 풀렸을거같긴한데, 공부도 하는김에
사람들의 풀이를 참조하여 bfs로 풀었다.

이 방식은 이렇다.
visited를 쓰며, deque를 활용한다. (bfs 니깐)

처음에 1번 노드로 스타트를 하기 위해 q에 1을 넣고 시작한다.
그리고 아래의 코드를 돌리면 이 방식으로 q가 변화하게 된다.
[1] -> [3, 2] -> [6, 4, 5]

1번 노드에서 제일 멀리 있는 애들이란, q에 제일 마지막에 담기는 애들이랑 같은말이다.
그래서 [6, 4, 5]의 갯수가 답이 된다.

복습하자!!@#!@!@!

"""

from collections import deque

def solution(n, edge):
    graph, visited = {}, [False] * (n + 1)
    for a, b in edge:
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]

    q, visited[1] = deque([1]), True
    while q:
        answer = len(q)
        for i in range(answer):
            node = q.popleft()
            for daum in graph[node]:
                if not visited[daum]:
                    visited[daum] = True
                    q.append(daum)

    return answer