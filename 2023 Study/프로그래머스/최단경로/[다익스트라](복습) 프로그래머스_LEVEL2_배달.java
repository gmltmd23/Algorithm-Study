import java.util.*;

public class Main {
    private static Map<Integer, List<Node>> graph;
    private static int[] distance;

    static class Node implements Comparable<Node> {
        public int dest;
        public int cost;

        public Node(int dest, int cost) {
            this.dest = dest;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    public static void dijkstra() {
        distance[1] = 0;
        PriorityQueue<Node> q = new PriorityQueue<>();
        q.add(new Node(1, 0));

        while(!q.isEmpty()) {
            Node node = q.poll();
            if(node.cost < distance[node.dest]) {
                distance[node.dest] = node.cost;
                continue;
            }

            List<Node> nextNodeList = graph.get(node.dest);
            for (Node nextNode : nextNodeList) {
                int totalCost = node.cost + nextNode.cost;
                if(totalCost < distance[nextNode.dest]) {
                    distance[nextNode.dest] = totalCost;
                    q.add(new Node(nextNode.dest, totalCost));
                }
            }
        }
    }

    public static int solution(int N, int[][] road, int K) {
        graph = new HashMap<>();
        distance = new int[N + 1];
        for(int i = 1; i <= N; ++i) {
            graph.put(i, new LinkedList<>());
            distance[i] = Integer.MAX_VALUE;
        }

        for(int[] eachRoad : road) {
            int a = eachRoad[0];
            int b = eachRoad[1];
            int cost = eachRoad[2];

            graph.get(a).add(new Node(b, cost));
            graph.get(b).add(new Node(a, cost));
        }

        dijkstra();

        int answer = 0;
        for(int i = 1; i <= N; ++i) {
            if(distance[i] <= K)
                ++answer;
        }

        return answer;
    }

    public static void main(String[] args) {
        int n = 5;
        int[][] road = {{1,2,1}, {2,3,3}, {5,2,2}, {1,4,2}, {5,3,1}, {5,4,2}};
        int k = 3;
        System.out.println(solution(n, road, k));
    }
}