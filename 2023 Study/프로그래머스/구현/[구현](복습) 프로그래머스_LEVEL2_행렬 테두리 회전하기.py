def rotate(graph, eachQuery):
    x1, y1, x2, y2 = map(lambda x: x - 1, eachQuery)
    theSmallestValue, firstValue = int(1e9), graph[x1][y1]

    for x in range(x1, x2):
        graph[x][y1] = graph[x + 1][y1]
        theSmallestValue = min(theSmallestValue, graph[x][y1])

    for y in range(y1, y2):
        graph[x2][y] = graph[x2][y + 1]
        theSmallestValue = min(theSmallestValue, graph[x2][y])

    for x in range(x2, x1, -1):
        graph[x][y2] = graph[x - 1][y2]
        theSmallestValue = min(theSmallestValue, graph[x][y2])

    for y in range(y2, y1, -1):
        graph[x1][y] = graph[x1][y - 1]
        theSmallestValue = min(theSmallestValue, graph[x1][y])

    if (y1 + 1) <= y2:
        graph[x1][y1 + 1] = firstValue
        theSmallestValue = min(theSmallestValue, firstValue)

    return theSmallestValue

def solution(rows, columns, queries):
    graph = [[] for _ in range(rows)]
    for x in range(rows):
        for y in range(1, columns + 1):
            graph[x].append((x * columns) + y)

    answer = []
    for eachQuery in queries:
        answer.append(rotate(graph, eachQuery))

    return answer


rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))