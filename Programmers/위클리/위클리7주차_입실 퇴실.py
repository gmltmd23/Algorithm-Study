"""

프로그래머스 위클리 7주차_입실 퇴실

푸는 방법이 여러가지 존재할 것 같은 문제이다.
나는 큐,스택,리스트,집합 등을 사용하여 풀었다.

우선 enter, leave등을 써먹기 쉽게 deque로 바꿔준다. (큐처럼 활용하기 위해서)
기본적인 알고리즘은 leave[0]이 큐에 존재하면 그놈을 버려주고, 그렇지않으면 새로운애를 큐에 넣는것이다.

그 이후 가장 중요한점은 큐에 새로운 사람[i]을 집어넣을때, 만약 그 큐가 비어있던 큐라면 상관없지만
예를들어 3명이 이미 존재하고 있던 큐라고 해보자.

그 큐에 새로 들어가는 사람 입장에서는 그 3명이 다 처음만나는 사람이다.
그러므로 answer[i] += len(q)  [이 코드를 작성할 당시에는 새로운 사람[i]는 아직 큐에 들어가지 않은 상태이다.]
이제 큐에 새로운 사람을 넣고..

3명의 입장에서는 새로운 사람 한명을 만나게 되는것이다.
어차피 큐에 새로운 사람을 넣으면 오른쪽 맨끝부터 차게되니깐
for i in range(len(q) - 1) 이런식으로 맨끝을 제외한 나머지 사람들에게 answer[i] += 1 코드를 돌려준다.

그렇게 enter가 빌때까지 넣어주면 문제는 풀린다.

"""

from collections import deque

def solution(enter, leave):
    answer = [0] * len(enter)
    enter, leave = deque(enter), deque(leave)
    check, q = {enter[0]}, [enter.popleft()]

    while enter:
        if leave[0] in check:
            target = leave.popleft()
            check.remove(target)
            q.remove(target)
        else:
            target = enter.popleft()
            answer[target - 1] += len(q)
            check.add(target)
            q.append(target)
            for i in range(len(q) - 1):
                answer[q[i] - 1] += 1

    return answer

enter = [1,4,2,3]
leave = [2,1,3,4]
print(solution(enter, leave))