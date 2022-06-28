import sys

class Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, node, rt):
        if node.data < rt.data: # 노드값이 비교값보다 작을때
            if rt.left: # 왼쪽이 None이 아닐때
                self.insert_node(node, rt.left)
            else: # 왼쪽이 None 일때
                rt.left = node
        elif node.data > rt.data:
            if rt.right:
                self.insert_node(node, rt.right)
            else:
                rt.right = node
        else:
            raise KeyError("Node %d is already exist." % node)

    def find_value(self, value, rt):
        if rt:
            if value < rt.data:
                check = self.find_value(value, rt.left)
            elif value > rt.data:
                check = self.find_value(value, rt.right)
            elif value == rt.data:
                check = True
        else:
            check = False

        return check


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

n = int(sys.stdin.readline())
items = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

root_node = Node(items[0])
my_tree = Tree()
my_tree.root = root_node

for i in range(1, len(items)):
    my_tree.insert_node(Node(items[i]), my_tree.root)

for value in targets:
    check = my_tree.find_value(value, my_tree.root)
    if check:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')