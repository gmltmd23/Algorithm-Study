"""

백준 문제 9237번 이장님 초대

규칙 찾기 문제이다.
인터넷에 풀이를 보면, 트리를 써서 하라는둥 그렇지만 결국에는 규칙을 찾는 문제이다.
복습하자.

"""

import sys
input = sys.stdin.readline

n = int(input())
tree = sorted(list(map(int, input().split())), key = lambda x: -x)
for idx in range(len(tree)):
    tree[idx] = tree[idx] + idx + 1
print(max(tree) + 1)