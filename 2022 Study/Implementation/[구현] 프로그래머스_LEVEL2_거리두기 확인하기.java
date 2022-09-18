public class Main {
    private static int[][] direction = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
    // LRUD,  LU RU LD RD

    private static boolean checkCorona(int x, int y, char[][] graph) {
        for(int i = 0; i < 4; ++i) {
            int nx = (x + direction[i][0]);
            int ny = (y + direction[i][1]);
            if(nx < 0 || nx >= 5 || ny < 0 || ny >= 5)
                continue;
            if(graph[nx][ny] == 'P')
                return false;
            else if(graph[nx][ny] == 'O') {
                nx += direction[i][0];
                ny += direction[i][1];
                if(nx < 0 || nx >= 5 || ny < 0 || ny >= 5)
                    continue;
                if(graph[nx][ny] == 'P')
                    return false;
            }
        }

        for(int i = 4; i < 8; ++i) {
            int nx = (x + direction[i][0]);
            int ny = (y + direction[i][1]);
            if(nx < 0 || nx >= 5 || ny < 0 || ny >= 5)
                continue;
            if(graph[nx][ny] == 'P') {
                if(graph[x][ny] != 'X' || graph[nx][y] != 'X')
                    return false;
            }
        }

        return true;
    }

    public static int process(char[][] graph) {
        for(int x = 0; x < 5; ++x) {
            for(int y = 0; y < 5; ++y) {
                if(graph[x][y] != 'P')
                    continue;
                if(!checkCorona(x, y, graph))
                    return 0;
            }
        }

        return 1;
    }

    public static int[] solution(String[][] places) {
        int[] answer = {1, 1, 1, 1, 1};

        int order = 0;
        for(String[] place : places) {
            char[][] graph = new char[5][5];
            for(int i = 0; i < 5; ++i) {
                String line = place[i];
                for(int j = 0; j < 5; ++j)
                    graph[i][j] = line.charAt(j);
            }

            answer[order++] = process(graph);
        }

        return answer;
    }

    public static void main(String[] args) {
        String[][] places = {
                {"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
                {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
                {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
                {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
                {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}
        };

        int[] result = solution(places);
        System.out.print(result);
    }
}