def solution(n, results):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = [0] * (n + 1)

    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = -1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a == b or graph[a][b] != 0:
                    continue
                if graph[a][k] == graph[k][b]:
                    graph[a][b] = graph[a][k]

    answer = 0
    for i in range(1, n + 1):
        if graph[i][1:].count(0) == 1:
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))