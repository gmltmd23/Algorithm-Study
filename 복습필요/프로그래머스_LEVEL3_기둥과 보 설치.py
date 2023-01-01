DESTRUCT, CONSTRUCT = 0, 1
COLUMN, BEAM = 0, 1

def isEnable(frameSet):
    for x, y, structure in frameSet:
        if structure == COLUMN:
            if y == 0 or (x - 1, y, BEAM) in frameSet or (x, y, BEAM) in frameSet or (x, y - 1, COLUMN) in frameSet:
                continue
            return False
        elif structure == BEAM:
            if (x, y - 1, COLUMN) in frameSet or (x + 1, y - 1, COLUMN) in frameSet or (x - 1, y, BEAM) in frameSet and (x + 1, y, BEAM) in frameSet:
                continue
            return False
    return True

def solution(n, build_frame):
    frameSet = set()
    for x, y, structure, buildType in build_frame:
        eachFrame = (x, y, structure)
        if buildType == CONSTRUCT:
            frameSet.add(eachFrame)
            if not isEnable(frameSet):
                frameSet.remove(eachFrame)
        elif buildType == DESTRUCT:
            frameSet.remove(eachFrame)
            if not isEnable(frameSet):
                frameSet.add(eachFrame)

    answer = []
    for x, y, structure in frameSet:
        answer.append([x, y, structure])

    return sorted(answer)


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))