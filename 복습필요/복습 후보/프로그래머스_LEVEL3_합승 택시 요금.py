INF = int(1e9)

def floyd(distance, n):
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])


def solution(n, s, a ,b, fares):
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        distance[i][i] = 0

    for c, d, f in fares:
        distance[c][d], distance[d][c] = f, f

    floyd(distance, n)
    answer = INF
    for transfer in range(1, n + 1):
        if transfer == s:
            continue
        answer = min(answer, distance[s][transfer] + distance[transfer][a] + distance[transfer][b], distance[s][a] + distance[s][b])

    return answer

n = 6
s, a, b = 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))