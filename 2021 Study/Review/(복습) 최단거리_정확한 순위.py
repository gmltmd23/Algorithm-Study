"""

플로이드 워셜의 응용 문제이다
답을 알고나니깐 쉬운데, 처음에는 문제를 이해 못해서 고생좀 한 문제이다.
정확한 순위를 알수있는 학생이라는것은 모든 학생들과의 연결점(Edge)가 존재한다는 뜻이다.
즉 graph[i][j] != INF 이거나 graph[j][i] != INF 이면 edge가 존재한다는 의미이므로
저 조건을 만족할때마다 count를 증가시키고, 이 count가 학생의 수와 동일해지면
모든 학생과 연결된 Edge가 존재한다는 의미와 동일 하므로 학생의 정확한 순위를 알 수가 있다.

"""

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)