"""

프로그래머스 탐욕법(그리디)_섬 연결하기 : LEVEL 3

레벨3이지만, 쉬운문제이다. 최소신장트리(최소 스패닝 트리)를 구하는 문제이다.
물론 최소 신장 트리의 개념을 모르면 그 개념을 익혀야만 풀수있는 문제라 어렵겠지만
알고있다면 크루스칼 알고리즘으로 바로 풀 수 있다.

최소 신장 트리를 알기전에 개념을 정리해보자.

우선 사이클이다. 사이클이란 노드와 엣지를 가지는 그래프에서
노드가 1,2,3 이렇게 있고 1 -> 2, -> 3 -> 1 이런식으로 엣지가 이어져있으면
순환하기 때문에 사이클이 존재한다고 한다.

그 다음은 트리이다.
그래프의 일종인데, 여러 노드가 한 노드와 연결되있지않은 쉽게 얘기하자면
1:N은 가능하지만, N:1은 불가능하다. 왜냐하면 루트에서 리프로 내려가는 방향성이 존재하기 때문이다.

그리고 신장 트리이다.
그래프 내에 있는 모든 노드를 연결하고 사이클이 없는 그래프를 말한다.
같은 트리내에서도 신장 트리는 여러개가 발생할 수 있다.

마지막으로 최소 신장 트리는
신장 트리중에서 연결되있는 엣지의 비용합이 최소가 되는 트리를 말한다.
물론 최소신장트리도 여러개가 될 수도있다.

이 개념을 알고, find, union의 개념을 알면 풀수가 있다.

"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer, parent = 0, [_ for _ in range(n)]
    costs.sort(key=lambda x: x[2])

    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer