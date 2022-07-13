import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self._data = data
        self._left, self._right = None, None

    def addChild(self, child):
        if child._data == self._data:
            print("중복 데이터는 삽입할 수 없습니다.")
            return

        if child._data < self._data:
            if self._left is not None:
                self._left.addChild(child)
            else:
                self._left = child
        else:
            if self._right is not None:
                self._right.addChild(child)
            else:
                self._right = child

class BinarySearchTree:
    def __init__(self, root):
        self._root = root

    def getRootNode(self):
        return self._root

    def addChild(self, child):
        self._root.addChild(child)

    def preOrder(self, rootNode, result):
        result.append(rootNode._data)

        if rootNode._left is not None:
            self.preOrder(rootNode._left, result)

        if rootNode._right is not None:
            self.preOrder(rootNode._right, result)

    def inOrder(self, rootNode, result):
        if rootNode._left is not None:
            self.inOrder(rootNode._left, result)

        result.append(rootNode._data)

        if rootNode._right is not None:
            self.inOrder(rootNode._right, result)

    def postOrder(self, rootNode, result):
        if rootNode._left is not None:
            self.postOrder(rootNode._left, result)

        if rootNode._right is not None:
            self.postOrder(rootNode._right, result)

        result.append(rootNode._data)

nodeCandidateList = [5, 3, 9, 8, 1]
bst = BinarySearchTree(Node(7))
for nodeCandidate in nodeCandidateList:
    bst.addChild(Node(nodeCandidate))

preOrderResult, inOrderResult, postOrderResult = [], [], []
bst.preOrder(bst.getRootNode(), preOrderResult)
bst.inOrder(bst.getRootNode(), inOrderResult)
bst.postOrder(bst.getRootNode(), postOrderResult)

print(preOrderResult, inOrderResult, postOrderResult)