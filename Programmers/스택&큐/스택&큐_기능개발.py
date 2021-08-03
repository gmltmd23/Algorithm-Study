"""

프로그래머스 스택/큐_기능개발 : LEVEL 2

가벼운 문제였다. 옛~~날에 풀었던 적이 있는 문제인가보다 풀려있는거보니
그래도 알고리즘을 더 공부한 지금 풀으니깐 더 효율적인 풀이가 나온다.

progresses, speeds 이 2개의 리스트를 Deque로 바꿔주고 푸는편이 좋다.
그렇지않고 pop(0) 함수를 쓰면 pop을 하고나서, 다시 재정렬을 해줄때에도 O(n)에 시간복잡도를써서
시간복잡도가 O(n^2)가 나온다.

deque로 바꾸고 하면 O(n)으로 풀수있다.
아니면 리스트 자체를 reverse해준 뒤에 pop(0)말고 pop()을 하면 스택처럼 쓸수있어서
O(n + n) = O(n)으로 풀수있다.

"""

from collections import deque
def solution(progresses, speeds):
    result = []
    progresses, speeds = deque(progresses), deque(speeds)
    yesterday = ((100 - progresses[0]) // speeds[0]) + (1 if (100 - progresses[0]) % speeds[0] else 0)
    count = 0

    while progresses:
        progress, speed = progresses.popleft(), speeds.popleft()
        day = ((100 - progress) // speed) + (1 if (100 - progress) % speed > 0 else 0)
        if day <= yesterday:
            count += 1
        else:
            yesterday = day
            result.append(count)
            count = 1
    if count:
        result.append(count)

    return result

p = [80]
s = [5]
print(solution(p, s))