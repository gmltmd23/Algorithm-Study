import java.util.*;

class Main {
    static class Node implements Comparable {
        public int x;
        public int y;
        public int value;
        public Node parent;
        public Node left;
        public Node right;

        public Node(int x, int y, int value) {
            this.x = x;
            this.y = y;
            this.value = value;
        }

        @Override
        public int compareTo(Object other) {
            Node otherNode = (Node)other;

            if(this.y < otherNode.y)
                return 1;
            else if(this.y > otherNode.y)
                return -1;
            else
                return this.x - otherNode.x;
        }

        @Override
        public String toString() {
            return "[" + this.x + ", " + this.y + "]";
        }
    }

    static class Tree {
        public Node root;
        public ArrayList<ArrayList<Node>> level;

        public Tree(Node root) {
            this.root = root;
            level = new ArrayList<>();
            level.add(new ArrayList<>());
            level.get(0).add(root);
        }

        public void makeTree(ArrayList<Node> nodeList) {
            if(nodeList.size() <= 1)
                return;

            int beforeLevel = this.root.y;
            for(int i = 1; i < nodeList.size(); ++i) {
                Node eachNode = nodeList.get(i);
                if(beforeLevel != eachNode.y) {
                    level.add(new ArrayList<>());
                    beforeLevel = eachNode.y;
                }
                level.get(level.size() - 1).add(eachNode);
            }

            ArrayList<Node> underRootNodeList = level.get(1);
            for(Node eachNode : underRootNodeList) {
                if(eachNode.x < root.x)
                    root.left = eachNode;
                else
                    root.right = eachNode;
                eachNode.parent = root;
            }

            for(int i = 2; i < level.size(); ++i) {
                ArrayList<Node> parentNodeList = level.get(i - 1);
                ArrayList<Node> levelNodeList = level.get(i);
                for(Node eachNode : levelNodeList) {
                    int parentIndex = findParentIndex(i, eachNode);
                    Node parentNode = parentNodeList.get(parentIndex);
                    if(eachNode.x < parentNode.x)
                        parentNode.left = eachNode;
                    else
                        parentNode.right = eachNode;
                    eachNode.parent = parentNode;
                }
            }
        }

        public void preOrder(int[][] answer) {
            ArrayList<Integer> valueList = new ArrayList<>();
            preOrderInternal(this.root, valueList);

            answer[0] = new int[valueList.size()];
            for(int i = 0; i < valueList.size(); ++i)
                answer[0][i] = valueList.get(i);
        }

        public void postOrder(int[][] answer) {
            ArrayList<Integer> valueList = new ArrayList<>();
            postOrderInternal(this.root, valueList);

            answer[1] = new int[valueList.size()];
            for(int i = 0; i < valueList.size(); ++i)
                answer[1][i] = valueList.get(i);
        }

        private void preOrderInternal(Node nowNode, ArrayList<Integer> valueList) {
            if(nowNode == null)
                return;

            valueList.add(nowNode.value);
            preOrderInternal(nowNode.left, valueList);
            preOrderInternal(nowNode.right, valueList);
        }

        private void postOrderInternal(Node nowNode, ArrayList<Integer> valueList) {
            if(nowNode == null)
                return;

            postOrderInternal(nowNode.left, valueList);
            postOrderInternal(nowNode.right, valueList);
            valueList.add(nowNode.value);
        }

        private int findParentIndex(int nowLevelIndex, Node nowNode) {
            ArrayList<Node> parentLevel = level.get(nowLevelIndex - 1);
            int left = 0;
            int right = parentLevel.size() - 1;

            while(left <= right) {
                int mid = (left + right) / 2;
                Node candidateParentNode = parentLevel.get(mid);
                if(nowNode.x < candidateParentNode.x)
                    right = mid - 1;
                else
                    left = mid + 1;
            }

            if(left < 0 || left >= parentLevel.size())
                return right;
            else if(right < 0 || right >= parentLevel.size())
                return left;

            Node leftNode = parentLevel.get(left);
            Node rightNode = parentLevel.get(right);

            if(Math.abs(leftNode.x - nowNode.x) < Math.abs(rightNode.x - nowNode.x))
                return left;
            else
                return right;
        }
    }

    public static int[][] solution(int[][] nodeinfo) {
        ArrayList<Node> nodeList = new ArrayList<>();
        for(int i = 0; i < nodeinfo.length; ++i) {
            int[] eachNode = nodeinfo[i];
            nodeList.add(new Node(eachNode[0], eachNode[1], (i + 1)));
        }
        Collections.sort(nodeList);

        Tree tree = new Tree(nodeList.get(0));
        tree.makeTree(nodeList);

        int[][] answer = new int[2][];
        tree.preOrder(answer);
        tree.postOrder(answer);

        return answer;
    }

    public static void main(String[] args) {
        int[][] nodeInfo = {{5, 3}, {11, 5}, {13, 3}, {3, 5}, {6, 1}, {1, 3}, {8, 6}, {7, 2}, {2, 2}};
        int[][] answer = solution(nodeInfo);
        //System.out.println(solution(nodeInfo));
        for(int i = 0; i < answer.length; ++i) {
            for(int j = 0 ; j < answer[i].length; ++j) {
                System.out.print(answer[i][j] + ", ");
            }
            System.out.println();
        }
    }
}