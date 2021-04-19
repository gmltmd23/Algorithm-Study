"""

시간이 오래걸리는 문제이므로, 시간을 줄일수 있도록 실력을 더 키우자

"""

import sys
import copy
input = sys.stdin.readline

def solution(s):
    length = len(s)
    maximum = (length // 2) + 1
    checker = [[0] * (length) for _ in range(maximum + 1)]
    result = 1001

    for limit in range(1, maximum):
        compare, start, end = 0, limit, 2 * limit
        while end <= length:
            word = s[compare: compare + limit]
            if word == s[start: end]:
                checker[limit][compare] += 1
            else:
                compare = start
            start, end = (start + limit), (end + limit)

    for i in range(1, maximum):
        temp = copy.deepcopy(s)
        for j in range(len(checker[i])):
            if checker[i][j] != 0:
                count = checker[i][j] + 1
                temp = temp.replace(count * s[j: j + i], str(count) + s[j: j + i])
                if len(temp) < result:
                    result = len(temp)

    return length if result == 1001 else result

tt = "xababcdcdababcdcd"
print(solution(tt))