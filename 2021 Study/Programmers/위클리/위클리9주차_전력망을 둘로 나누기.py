"""

프로그래머스 위클리 9주차_전력망을 둘로 나누기

9주차로 올라온 문제이다.
처음에는 Indegree가 제일 많은 노드를 찾고 거기서 dfs를 하여 노드의 개수가
제일 많은 네트워크망의 엣지를 잘라주는건줄 알고 풀었는데 100점만점에 54점이 나왔다.
그렇게 푸는게 아니란 뜻이다.

그리고 생각난 방법은 서로소집합을 이용하는 방법이다.
이 방법을 사용하게 되면 서로 연결되있는 노드끼리는 parent가 서로 같게끔 나온다. (내가 짜놓은 대로하면 서로 연결되있는것끼리는 결국 부모가 1로 나온다.)
즉 주어진 엣지들중에 한개씩 제외해가면서 서로소집합 방법을 돌리면 각각 엣지를 제외할때마다
나오는 parents의 1의 개수가 한개의 엣지를 제외했을때 따로 생기는 전력망의 노드 개수이다.

문제에서 요구하는건 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)중 최소값을 원하므로
최소값을 구해주면 정답이 된다.
자바로도 풀어봐야겠다.

"""

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, wires):
    answer = 1e9
    for i in range(len(wires)):
        parents = [_ for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue # 이게 한 개의 엣지를 제외하고서 생각하는 행위이다.
            a, b = wires[j][0], wires[j][1]
            union(parents, a, b)
        for idx in range(1, n + 1):
            find_parent(parents, idx)

        print(parents)
        sub = parents.count(1)
        if abs((n - sub) - sub) < answer:
            answer = abs((n - sub) - sub)
    return answer



n = 4
wires = [[1,2],[2,3],[3,4]]
print(solution(n, wires))