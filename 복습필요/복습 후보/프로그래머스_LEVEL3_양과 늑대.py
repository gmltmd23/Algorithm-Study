def solution(info, edges):
    visited = [False] * len(info)
    visited[0] = True
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for parent, child in edges:
            isWolf = True if info[child] == 1 else False
            if visited[parent] and not visited[child]:
                visited[child] = True
                dfs(sheep + (not isWolf), wolf + isWolf)
                visited[child] = False

    dfs(1, 0)

    return max(answer)



info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))