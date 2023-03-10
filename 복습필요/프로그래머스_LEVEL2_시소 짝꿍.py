def innerCheck(weight, targetWeight, weightCounter, pairSet):
    if weight == targetWeight and weightCounter[weight] >= 2:
        pair = (weight, weight)
        if pair not in pairSet:
            pairSet.add(pair)
    elif weight != targetWeight:
        pair = (min(weight, targetWeight), max(weight, targetWeight))
        if pair not in pairSet:
            pairSet.add(pair)

def check(weight, targetSet, weightCounter, pairSet, magnification):
    time2, time3, time4 = (weight * 2), (weight * 3), (weight * 4)
    if time2 in targetSet:
        innerCheck(weight, time2 / magnification, weightCounter, pairSet)
    if time3 in targetSet:
        innerCheck(weight, time3 / magnification, weightCounter, pairSet)
    if time4 in targetSet:
        innerCheck(weight, time4 / magnification, weightCounter, pairSet)

def solution(weights):
    two, three, four = set(), set(), set()
    weightCounter = dict()
    for weight in weights:
        two.add(weight * 2)
        three.add(weight * 3)
        four.add(weight * 4)
        if weight not in weightCounter:
            weightCounter[weight] = 0
        weightCounter[weight] += 1

    pairSet = set()
    for weight in weights:
        check(weight, two, weightCounter, pairSet, 2)
        check(weight, three, weightCounter, pairSet, 3)
        check(weight, four, weightCounter, pairSet, 4)

    return len(pairSet)

weights = [100, 180, 360, 100, 270]
print(solution(weights))