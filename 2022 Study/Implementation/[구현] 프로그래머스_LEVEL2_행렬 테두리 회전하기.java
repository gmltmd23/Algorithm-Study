public class Main {
    public static int[] solution(int rows, int columns, int[][] queries) {
        int[][] graph = new int[rows][columns];
        for(int i = 1; i <= rows; ++i) {
            for(int j = 1; j <= columns; ++j)
                graph[i - 1][j - 1] = ((i - 1) * columns + j);
        }

        int[] answer = new int[queries.length];

        for(int i = 0; i < queries.length; ++i) {
            int[] query = queries[i];
            int x1 = query[0] - 1;
            int y1 = query[1] - 1;
            int x2 = query[2] - 1;
            int y2 = query[3] - 1;

            int firstPlaceValue = graph[x1][y1];
            int minimumValue = 10000;
            for(int nowX = x1; nowX < x2; ++nowX) {
                minimumValue = Math.min(minimumValue, graph[nowX + 1][y1]);
                graph[nowX][y1] = graph[nowX + 1][y1];
            }

            for(int nowY = y1; nowY < y2; ++nowY) {
                minimumValue = Math.min(minimumValue, graph[x2][nowY + 1]);
                graph[x2][nowY] = graph[x2][nowY + 1];
            }

            for(int nowX = x2; nowX > x1; --nowX) {
                minimumValue = Math.min(minimumValue, graph[nowX - 1][y2]);
                graph[nowX][y2] = graph[nowX - 1][y2];
            }

            for(int nowY = y2; nowY > y1; --nowY) {
                minimumValue = Math.min(minimumValue, graph[x1][nowY - 1]);
                graph[x1][nowY] = graph[x1][nowY - 1];
            }

            graph[x1][y1 + 1] = firstPlaceValue;
            minimumValue = Math.min(minimumValue, firstPlaceValue);

            answer[i] = minimumValue;
        }

        return answer;
    }

    public static void main(String[] args) {
        int rows = 6;
        int columns = 6;
        int[][] queries = {{2,2,5,4},{3,3,6,6},{5,1,6,3}};

        int[] result = solution(rows, columns, queries);
    }
}