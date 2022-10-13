def solution(n, stations, w):
    supportCoverage = 2 * w + 1
    answer, nowPosition = 0, 1
    for station in stations:
        left, right = (station - w - 1), (station + w + 1)
        if nowPosition <= left:
            needCoverage = (left - nowPosition) + 1
            answer += needCoverage // supportCoverage
            answer += 1 if needCoverage % supportCoverage != 0 else 0
        nowPosition = right

    if nowPosition <= n:
        needCoverage = (n - nowPosition) + 1
        answer += needCoverage // supportCoverage
        answer += 1 if needCoverage % supportCoverage != 0 else 0

    return answer