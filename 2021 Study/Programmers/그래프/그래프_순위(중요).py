def solution(n, results):
    wins, loses = {}, {}
    for i in range(1, n + 1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n + 1):
        for winner, loser in results:
            if winner == i:
                wins[i].add(loser)
            if loser == i:
                loses[i].add(winner)

        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])

    cnt = 0
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            cnt += 1

    return cnt

n = 5
r = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n , r))