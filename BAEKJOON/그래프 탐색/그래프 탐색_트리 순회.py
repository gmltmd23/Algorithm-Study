"""

백준 1991 트리 순회

코딩테스트에서 자주 나오는 문제는 아니지만, 개념은 익혀둬야 하니깐
우선 풀었다.

트리를 class로 만들지않고, dictionary로 만들어서 접근속도를 O(1)로 만들어 주는것이
핵심인 문제였다.

전위, 중위, 후휘 순회의 개념을 알면 print()의 순서만 바꿔도 풀수있는 문제

"""

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def pre_order(tree, node):
    print(node.data, end = '')
    if node.left != '.':
        pre_order(tree, tree[node.left])
    if node.right != '.':
        pre_order(tree, tree[node.right])

def in_order(tree, node):
    if node.left != '.':
        in_order(tree, tree[node.left])
    print(node.data, end = '')
    if node.right != '.':
        in_order(tree, tree[node.right])

def post_order(tree, node):
    if node.left != '.':
        post_order(tree, tree[node.left])
    if node.right != '.':
        post_order(tree, tree[node.right])
    print(node.data, end = '')

def solution(tree):
    pre_order(tree, tree['A'])
    print()
    in_order(tree, tree['A'])
    print()
    post_order(tree, tree['A'])

def main():
    n = int(input().rstrip())
    tree = {}
    for i in range(n):
        data, left, right = map(str, input().split())
        tree[data] = Node(data, left, right)
    solution(tree)

main()