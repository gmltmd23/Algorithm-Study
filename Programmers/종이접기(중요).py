"""

프로그래머스 종이접기 (Level3) 문제

처음에는 트리를 만들고, 중위순회를 해서 푸는문제 인가 싶어서 풀어봤다.
아 근데 가볍게틀림 그래서 다른 방식으로 만들어보기로 했다.


import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root = None):
        self.root = root

    def add_node(self, node, n):
        if n > 1:
            if node.left is None:
                node.left = Node(0)
                self.add_node(node.left, n - 1)
            if node.right is None:
                node.right = Node(1)
                self.add_node(node.right, n - 1)

    def pre_order(self, nd):
        if nd is not None:
            print(nd.val, end = ' ')
            if nd.left:
                self.pre_order(nd.left)
            if nd.right:
                self.pre_order(nd.right)

    def in_order(self, nd):
        if nd is not None:
            if nd.left:
                self.pre_order(nd.left)
            print(nd.val, end = ' ')
            if nd.right:
                self.pre_order(nd.right)

def solution(n):
    t = Tree(Node(0))
    t.add_node(t.root, n)
    t.in_order(t.root)

solution(3)

"""


"""

밑에 코드처럼 하니깐 맞았다.

"""

def convert(answer):
    temp = []
    for a in answer:
        if a == 0:
            temp.append(1)
        else:
            temp.append(0)
    return temp

def solution(n):
    answer = [0]
    for i in range(1, n):
        temp = convert(answer[::-1])
        answer.append(0)
        answer += temp
    return answer

print(solution(4))