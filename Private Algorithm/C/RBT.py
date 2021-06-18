import sys

sys.setrecursionlimit(10 ** 4)


def dfs(graph, visited, red_colors, root):
    for child in graph[root]:
        if not visited[child]:
            visited[child] = True
            if root not in red_colors:
                red_colors.append(child)
            else:
                flag = False
                for grand_child in graph[child]:
                    if len(graph[grand_child]) - 1 == 0:
                        flag = True
                        break
                if flag:
                    red_colors.append(child)
            dfs(graph, visited, red_colors, child)


def hospital(city_nodes, city_from, city_to):  # Red Black Tree를 변형해서 풉니다.
    graph = [[] for _ in range(city_nodes + 1)]
    visited = [False] * (city_nodes + 1)
    red_colors = []
    for a, b in zip(city_from, city_to):
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, city_nodes + 1):
        if len(graph[i]) == 1:
            root = i
            visited[root] = True
            break
    dfs(graph, visited, red_colors, root)

    return len(red_colors)


"""
g1, g2 = [], []
for i in range(110):
    a, b = map(int, input().split())
    g1.append(a)
    g2.append(b)
print(hospital(111, g1, g2))
"""


print(hospital(2, [1], [2]))

print(hospital(12, [1, 1, 6, 1, 1, 2, 11, 12, 4, 12, 6], [11, 2, 7, 6, 12, 3, 10, 9, 5, 8, 4]))
print(hospital(4, [1, 2, 3], [2, 3, 4]))
print(hospital(7, [1, 3, 1, 3, 2, 1], [2, 6, 4, 7, 5, 3]))