PILLAR, PAPER = 0, 1
DELETE, CONSTRUCT = 0, 1

def canConstruct(graphSet):
    for x, y, type in graphSet:
        if type == PILLAR:
            if (y == 0) or (x, y - 1, PILLAR) in graphSet or (x - 1, y, PAPER) in graphSet or (x, y, PAPER) in graphSet:
                continue
            return False
        elif type == PAPER:
            if ((x + 1, y, PAPER) in graphSet and (x - 1, y, PAPER) in graphSet) or (x, y - 1, PILLAR) in graphSet or (x + 1, y - 1, PILLAR) in graphSet:
                continue
            return False
    return True

def solution(n, build_frame):
    graphSet = set()
    for x, y, type, op in build_frame:
        if op == CONSTRUCT:
            graphSet.add((x, y, type))
            if not canConstruct(graphSet):
                graphSet.remove((x, y, type))
        elif op == DELETE:
            graphSet.remove((x, y, type))
            if not canConstruct(graphSet):
                graphSet.add((x, y, type))

    return sorted(list(graphSet))


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))