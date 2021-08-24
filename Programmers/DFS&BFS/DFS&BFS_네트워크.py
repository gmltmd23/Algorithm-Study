"""

프로그래머스 DFS&BFS_네트워크 : LEVEL 3

평상시에 DFS&BFS 문제를 연습했다면, 쉽게 풀수있는 문제였다.
컴퓨터 갯수만큼 루프문을 돌려준다.
루프를 돌려줄때, 컴퓨터 자기자신이 1이면 answer += 1, 0이면 카운팅 안해주는방식으로
dfs 알고리즘을 짜면된다.

dfs 알고리즘에 들어가서는, 1인것들은 모두 0으로 바꿔주게끔 만들면 끝

"""

def dfs(n, computers, i):
    if computers[i][i] == 1:
        computers[i][i] = 0
    for j in range(n):
        if computers[i][j] == 1:
            computers[i][j] = 0
            dfs(n, computers, j)

def solution(n, computers):
    answer = 0
    for i in range(n):
        if computers[i][i] == 1:
            dfs(n, computers, i)
            answer += 1
    return answer

n = 3
c = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, c))