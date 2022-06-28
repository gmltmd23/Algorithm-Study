import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

test_cases = int(input().rstrip())
dx = [0, -1, 1] # 오른쪽, 오른쪽위, 오른쪽아래
result = []
for i in range(test_cases):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    index = 0
    for j in range(n):
        for k in range(m):
            graph[j].append(golds[index])
            index += 1
    max_value = -1
    for b in range(m):
        for a in range(n):
            temp = graph[a][b]
            for dim in range(3):
                nx, ny = (a + dx[dim]), (b - 1)
                if 0 <= nx < n and 0 <= ny < m:
                    graph[a][b] = max(graph[a][b], graph[nx][ny] + temp)
            max_value = max(max_value, graph[a][b])
    result.append(max_value)

for res in result:
    print(res)