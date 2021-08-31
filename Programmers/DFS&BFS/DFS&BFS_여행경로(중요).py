"""

프로그래머스 DFS&BFS_여행경로 : LEVEL 3

DFS문제중 어려운 문제이다.
stack을 써서 풀게 되었는데, while문 안에서 else 조건절이 중요하다.
if 조건에 해당하지 않을 경우 answer에 stack.pop()을 append 해주는데
이거는 언젠가는 방문할 loc지만 지금 방문해버리면 티켓을 모두쓰지않고, 여행경로를 마쳐버리는 애들이다.

걔네들을 그럼 마지막에 방문하면 될테니 answer에 append를 해주는것이다. (어차피 answer은 마지막에 reverse 한번 해줄거니깐 맨 처음으로 들어간애들이 맨 마지막 애들이됌)
개념이 중요한 문제였다. 복습하자.

"""

def solution(tickets):
    answer, from_to = [], {}
    for ticket in tickets:
        from_to[ticket[0]] = from_to.get(ticket[0], []) + [ticket[1]]
    for key in from_to:
        from_to[key].sort(reverse=True)
    stack = ["ICN"]

    while stack:
        loc = stack[-1]
        if loc in from_to and from_to[loc]:
            stack.append(from_to[loc].pop())
        else:
            answer.append(stack.pop())

    answer.reverse()
    return answer