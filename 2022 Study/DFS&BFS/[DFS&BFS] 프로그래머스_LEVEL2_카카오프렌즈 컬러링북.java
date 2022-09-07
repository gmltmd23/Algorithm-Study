import java.util.HashMap;
import java.util.HashSet;

public class Main {
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
    private static int gatherValue, maxSizeOfOneArea;
    private static boolean[][] visited;

    public static void dfs(int x, int y, int m, int n, int[][] picture) {
        int nowNumberOfArea = picture[x][y];
        for(int i = 0; i < 4; ++i) {
            int nx = (x + dx[i]);
            int ny = (y + dy[i]);
            if(0 <= nx && nx < m && 0 <= ny && ny < n) {
                if(visited[nx][ny] == false && nowNumberOfArea == picture[nx][ny]) {
                    visited[nx][ny] = true;
                    ++gatherValue;
                    dfs(nx, ny, m, n, picture);
                }
            }
        }
    }

    public static int[] solution(int m, int n, int[][] picture) {
        maxSizeOfOneArea = 0;
        visited = new boolean[m][n];
        HashSet<Integer> checkSet = new HashSet<>();

        for(int x = 0; x < m; ++x) {
            for(int y = 0; y < n; ++y) {
                checkSet.add(picture[x][y]);
                if(!visited[x][y] && picture[x][y] != 0) {
                    gatherValue = 1;
                    visited[x][y] = true;
                    dfs(x, y, m, n, picture);
                    if(maxSizeOfOneArea < gatherValue)
                        maxSizeOfOneArea = gatherValue;
                    gatherValue = 0;
                }
            }
        }

        int[] answer = {checkSet.size(), maxSizeOfOneArea};

        return answer;
    }

    public static void main(String[] args) {
        int m = 6;
        int n = 4;
        int[][] picture = {
                {1,1,1,0},
                {1,2,2,0},
                {1,0,0,1},
                {0,0,0,1},
                {0,0,0,3},
                {0,0,0,3}
        };

        int[] result = solution(m, n, picture);
        for(int element : result) {
            System.out.println("결과 : " + element);
        }
    }
}