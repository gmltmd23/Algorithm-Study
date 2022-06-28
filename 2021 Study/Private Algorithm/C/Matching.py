def dfs(graph, pos, temp):
    temp.add(pos)
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    x, y = pos
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(graph, (nx, ny), temp)

def make_graph(grid):
    graph = [[] for _ in range(len(grid))]
    for i in range(len(graph)):
        graph[i] = list(map(int, ' '.join(str(grid[i])).split()))
    return graph


def countMatches(grid1, grid2):
    grid1, grid2 = make_graph(grid1), make_graph(grid2)
    g1_group, g2_group = [], []
    for x in range(len(grid1)):
        for y in range(len(grid1[0])):
            g1_temp = set()
            if grid1[x][y] == 1:
                grid1[x][y] = 0
                dfs(grid1, (x, y), g1_temp)
                g1_group.append(g1_temp)
            g2_temp = set()
            if grid2[x][y] == 1:
                grid2[x][y] = 0
                dfs(grid2, (x, y), g2_temp)
                g2_group.append(g2_temp)

    count = 0
    if len(g1_group) <= len(g2_group):
        a, b = g1_group, g2_group
    else:
        a, b = g2_group, g1_group

    for element in a:
        if element in b:
            count += 1

    return count