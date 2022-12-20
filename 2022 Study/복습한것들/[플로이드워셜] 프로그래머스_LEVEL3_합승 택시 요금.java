public class Main {
    private static int[][] graph;

    public static void floyd(int n) {
        for(int k = 1; k < (n + 1); ++k) {
            for(int i = 1; i < (n + 1); ++i) {
                for (int j = 1; j < (n + 1); ++j)
                    graph[i][j] = Math.min(graph[i][j], (graph[i][k] + graph[k][j]));
            }
        }
    }

    public static int solution(int n, int s, int a, int b, int[][] fares) {
        graph = new int[n + 1][n + 1];
        for(int x = 1; x < (n + 1); ++x) {
            for(int y = 1; y < (n + 1); ++y)
                graph[x][y] = (x == y) ? 0 : 1000000;
        }

        for(int[] eachFare : fares) {
            int c = eachFare[0];
            int d = eachFare[1];
            int f = eachFare[2];
            graph[c][d] = f;
            graph[d][c] = f;
        }

        floyd(n);

        int totalCost = graph[s][a] + graph[s][b];
        for(int i = 1; i < n + 1; ++i)
            totalCost = Math.min(totalCost, (graph[s][i] + graph[i][a] + graph[i][b]));

        return totalCost;
    }

    public static void main(String[] args) {
        int n = 6;
        int s = 4;
        int a = 6;
        int b = 2;
        int[][] fares = {{4, 1, 10}, {3, 5, 24}, {5, 6, 2}, {3, 1, 41}, {5, 1, 24}, {4, 6, 50}, {2, 4, 66}, {2, 3, 22}, {1, 6, 25}};
        System.out.println(solution(n, s, a, b, fares));
    }
}