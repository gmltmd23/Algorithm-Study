from collections import deque

def solution(priorities, location):
    wonderEggs = deque()
    sortedPriorities = sorted(priorities)
    for loc, p in enumerate(priorities):
        wonderEggs.append([p, loc])

    count = 0
    while sortedPriorities:
        maximumPriority = sortedPriorities[-1]
        while len(sortedPriorities) == len(wonderEggs):
            egg = wonderEggs.popleft()
            if egg[0] != maximumPriority:
                wonderEggs.append(egg)
            else:
                count += 1
                if egg[1] == location:
                    return count
        sortedPriorities.pop()